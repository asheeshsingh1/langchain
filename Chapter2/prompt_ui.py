from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation"
)
model = ChatHuggingFace(llm=model)

st.header("Research Tool")

cricketer = st.selectbox(
    "Select Cricketer", ["Virat Kohli", "MS Dhoni", "Yuvraj Singh"]
)
age = st.selectbox("Select life", ["child", "young", "retired"])
size = st.selectbox("Select para count", [1, 2, 3])

template = PromptTemplate(
    template="Tell me a story about {cricketer} when he was {age}. In {size} paraghaph.",
    input_variables=["cricketer", "age", "size"],
)

if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({"cricketer": cricketer, "size": size, "age": age})
    st.write(result.content)
