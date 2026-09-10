from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="Give me 2 line facts about {topic}. {format}",
    input_variables=["topic"],
    partial_variables={"format": parser.get_format_instructions()},
)

chain = prompt | model | parser

result = chain.invoke({"topic": "blackhole"})

print(result)
