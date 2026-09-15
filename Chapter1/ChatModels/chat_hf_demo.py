from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation"
)

model = ChatHuggingFace(llm=model)

result = model.invoke("Capital of India?")
print(result.content)
