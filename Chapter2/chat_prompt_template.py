# from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

# It does not work like this in prompt templates
# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert"),
#     HumanMessage(content="Explain in simple terms what is {topic}")
# ])

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful {domain} expert"),
        ("human", "Explain in simple terms what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "Cricket", "topic": "Dusra"})

print(prompt)
