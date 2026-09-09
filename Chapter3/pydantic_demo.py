from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class City(BaseModel):
    name: str
    state: Optional[str] = Field(description="State in which this city is situated.")


model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

structured_model = model.with_structured_output(City)

result = structured_model.invoke("Most Populated city in India")
print(result)
