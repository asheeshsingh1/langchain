from dotenv import load_dotenv
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi

load_dotenv()


def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text


video_id = "Gfr50f6ZBvo"  # only the ID, not full URL
try:
    # If you don’t care which language, this returns the “best” one
    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id, languages=["en"])

    transcript_list = transcript.to_raw_data()

    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)

except TranscriptsDisabled:
    print("No captions available for this video.")


splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
vector_store = FAISS.from_documents(chunks, embeddings)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})


llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

prompt = PromptTemplate(
    template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
    """,
    input_variables=["context", "question"],
)

parallel_chain = RunnableParallel(
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough(),
    }
)

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

result = main_chain.invoke("Can you summarize the video")

print(result)
