from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

source = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]

question = "capital of west?"

query = embedding.embed_query(question)
vector = embedding.embed_documents(source)

scores = cosine_similarity([query], vector)[0]
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(question)
print(source[index])
print("Similarity: ", float(score * 100))
