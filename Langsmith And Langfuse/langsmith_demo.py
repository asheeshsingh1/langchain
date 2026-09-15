from langsmith import traceable
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langfuse.langchain import CallbackHandler
from langfuse import get_client

client = get_client()

load_dotenv()

langfuse_handler = CallbackHandler()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")


@traceable(run_type="llm")
def chat(message: str):
    result = llm.invoke(
        message,
        config={
            "callbacks": [langfuse_handler],
        },
    )

    return result


print(chat("Hello from Asheesh."))

client.flush()
