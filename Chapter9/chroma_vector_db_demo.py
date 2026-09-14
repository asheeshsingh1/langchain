from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_classic.schema import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


# ---------------------------------------------------------
# 1. Create Documents
# ---------------------------------------------------------

doc1 = Document(
    page_content=(
        "Virat Kohli is one of the most successful and consistent "
        "batsmen in IPL history. Known for his aggressive batting style "
        "and fitness, he has led the Royal Challengers Bangalore in "
        "multiple seasons."
    ),
    metadata={"team": "Royal Challengers Bangalore"},
)

doc2 = Document(
    page_content=(
        "Rohit Sharma is the most successful captain in IPL history, "
        "leading Mumbai Indians to five titles. He's known for his calm "
        "demeanor and ability to play big innings under pressure."
    ),
    metadata={"team": "Mumbai Indians"},
)

doc3 = Document(
    page_content=(
        "MS Dhoni, famously known as Captain Cool, has led Chennai Super "
        "Kings to multiple IPL titles. His finishing skills, wicketkeeping, "
        "and leadership are legendary."
    ),
    metadata={"team": "Chennai Super Kings"},
)

doc4 = Document(
    page_content=(
        "Jasprit Bumrah is considered one of the best fast bowlers in "
        "T20 cricket. Playing for Mumbai Indians, he is known for his "
        "yorkers and death-over expertise."
    ),
    metadata={"team": "Mumbai Indians"},
)

doc5 = Document(
    page_content=(
        "Ravindra Jadeja is a dynamic all-rounder who contributes with "
        "both bat and ball. Representing Chennai Super Kings, his quick "
        "fielding and match-winning performances make him a key player."
    ),
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3, doc4, doc5]


# ---------------------------------------------------------
# 2. Create Embedding Model
# ---------------------------------------------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
)


# ---------------------------------------------------------
# 3. Create Chroma Vector Store
# ---------------------------------------------------------

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="ipl_players",
)


# ---------------------------------------------------------
# 4. Semantic Similarity Search
# ---------------------------------------------------------

print("\n========== SIMILARITY SEARCH ==========\n")

results = vector_store.similarity_search(
    query="Any all rounder out there?",
    k=1,
)

for doc in results:
    print("Document:")
    print(doc.page_content)

    print("\nMetadata:")
    print(doc.metadata)

    print("-" * 80)


# ---------------------------------------------------------
# 5. Similarity Search With Score
# ---------------------------------------------------------

print("\n========== SIMILARITY SEARCH WITH SCORE ==========\n")

results = vector_store.similarity_search_with_score(
    query="Who among these is a bowler?",
    k=2,
)

for doc, score in results:
    print("Document:")
    print(doc.page_content)

    print("\nMetadata:")
    print(doc.metadata)

    print("\nScore:")
    print(score)

    print("-" * 80)


# ---------------------------------------------------------
# 6. Similarity Search + Metadata Filter
# ---------------------------------------------------------

print("\n========== SIMILARITY SEARCH + FILTER ==========\n")

results = vector_store.similarity_search_with_score(
    query="Who is an all rounder?",
    k=2,
    filter={"team": "Chennai Super Kings"},
)

for doc, score in results:
    print("Document:")
    print(doc.page_content)

    print("\nMetadata:")
    print(doc.metadata)

    print("\nScore:")
    print(score)

    print("-" * 80)


# ---------------------------------------------------------
# 7. Metadata Filtering WITHOUT Similarity Search
# ---------------------------------------------------------

print("\n========== METADATA FILTER ONLY ==========\n")

result = vector_store.get(
    where={"team": "Chennai Super Kings"},
)

for document, metadata in zip(
    result["documents"],
    result["metadatas"],
):
    print("Document:")
    print(document)

    print("\nMetadata:")
    print(metadata)

    print("-" * 80)


# ---------------------------------------------------------
# 8. Get Documents + Metadata + Embeddings
# ---------------------------------------------------------

print("\n========== GET ALL DATA ==========\n")

result = vector_store.get(
    include=[
        "documents",
        "metadatas",
        "embeddings",
    ],
)

print("Documents:")
print(result["documents"])

print("\nMetadata:")
print(result["metadatas"])

print("\nEmbeddings:")
print(result["embeddings"])
