from langfuse import get_client
from langfuse.langchain import CallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

client = get_client()
langfuse_handler = CallbackHandler()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)

response = llm.invoke(
    "What is the capital of India?",
    config={
        "callbacks": [langfuse_handler],
    },
)

print(response.content)
