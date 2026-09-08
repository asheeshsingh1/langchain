from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

model = HuggingFaceEndpointEmbeddings(
    repo_id="google/embeddinggemma-300m"
)

docs = [
    "Asheesh loves to eat food.",
    "Asheesh works as a software engineer.",
    "Asheesh Lives in moradabad.",
]
question = "what does asheesh works as?"

# query = model.embed_query("Asheesh is a good boy")
source = model.embed_documents(docs)
query = model.embed_query(question)

scores = cosine_similarity([query], source)[0]
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]


print(question)
print(docs[index])
print("Similarity: ",float(score * 100))