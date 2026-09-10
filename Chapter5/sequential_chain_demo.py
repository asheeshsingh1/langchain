from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation"
)

model1 = ChatHuggingFace(llm=llm)

model2 = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write {lines_count} of story about {person}.",
    input_variables=["lines_count", "person"],
)

prompt2 = PromptTemplate(
    template="Summarize given {text} in 1 line.", input_variables=["text"]
)

chain = prompt1 | model2 | parser | prompt2 | model2 | parser

result = chain.invoke({"lines_count": 3, "person": "Narendra Modi"})

print(result)

chain.get_graph().print_ascii()
