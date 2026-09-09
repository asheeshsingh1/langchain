from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()


class Capital(TypedDict):
    city: Annotated[str, "Capital city is also known as national capital."]
    region: Annotated[str, "Region is area like NCR, Northern India etc"]


model = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation"
    )
)

gemini = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

structured_model = model.with_structured_output(Capital)
structured_model1 = gemini.with_structured_output(Capital)

# result = structured_model.invoke("What is the capital city of India?")
result1 = structured_model1.invoke("What is Cappital of India?")

print(result1)
