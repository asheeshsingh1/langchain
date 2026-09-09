from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langsmith import traceable

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation"
)

model = ChatHuggingFace(llm=model)

messages = [SystemMessage(content="Welcome to the ChatBot")]


@traceable(run_type="llm")
def chat(greet: str):
    print(greet)
    while True:
        user_message = input("You: ")
        messages.append(HumanMessage(content=user_message))
        if user_message == "exit":
            break
        result = model.invoke(user_message)
        messages.append(AIMessage(content=result.content))
        print("AI: ", result.content)


chat("Welcome to chatbot")
print(messages)
