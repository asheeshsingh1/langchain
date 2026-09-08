from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-3.5-flash", google_api_key=os.getenv("GEMINI_API_KEY")
)

res = llm.invoke("capital of delhi")
print(res)
