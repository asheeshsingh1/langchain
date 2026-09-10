from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
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

prompt1 = PromptTemplate(
    template="3 imp learnings from {cricketer} life.", input_variables=["cricketer"]
)

prompt2 = PromptTemplate(
    template="3 imp learnings from {actor} life.", input_variables=["actor"]
)

prompt3 = PromptTemplate(
    template="Similarity between these 2 people's life learning: {learning1} /n {learning2}.",
    input_variables=["learning1", "learning2"],
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {"learning1": prompt1 | model1 | parser, "learning2": prompt2 | model2 | parser}
)

merge_chain = prompt3 | model2 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"cricketer": "virat kohli", "actor": "akshay kumar"})

print(result)

chain.get_graph().print_ascii()
