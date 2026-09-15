from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a Linkedin post about {topic}", input_variables=["topic"]
)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model, parser),
        "linkedin": RunnableSequence(prompt2, model, parser),
    }
)

result = parallel_chain.invoke({"topic": "AI"})

print(result["tweet"])
print(result["linkedin"])
