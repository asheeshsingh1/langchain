from typing import Optional

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Person(BaseModel):
    name: str
    city: Optional[str]
    age: Optional[int]


model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="generate a person named: {name}. {output_instruction}",
    input_variables=["name"],
    partial_variables={"output_instruction": parser.get_format_instructions()},
)

chain = template | model | parser

result = chain.invoke({"name": "Joseph"})

print(result)
