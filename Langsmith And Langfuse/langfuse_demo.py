from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langfuse import get_client
from langfuse.langchain import CallbackHandler
from pydantic import BaseModel, Field

load_dotenv()

client = get_client()
langfuse_handler = CallbackHandler()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)


class Capital(BaseModel):
    city_name: str
    language: str = Field(description="Language most of the people speak in that city.")


parser = PydanticOutputParser(pydantic_object=Capital)

prompt = PromptTemplate(
    template="What is the capital city of India? {format}",
    input_variables=[],
    partial_variables={"format": parser.get_format_instructions()},
)

chain = prompt | llm | parser

result = chain.invoke(
    {},
    config={
        "callbacks": [langfuse_handler],
    },
)

print(result)
print(result.city_name)
print(result.language)
