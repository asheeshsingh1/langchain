from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write {lines_count} of story about {person}.",
    input_variables=["lines_count", "person"],
)

chain = prompt | model | parser

result = chain.invoke({"lines_count": 3, "person": "Virat Kohli"})

print(result)

chain.get_graph().print_ascii()
