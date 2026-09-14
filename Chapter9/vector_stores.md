## What are Vector Stores
A vector store is a system designed to store and retrieve data represented as numerical
vectors.
Key Features
1. Storage – Ensures that vectors and their associated metadata are retained, whether inmemory for quick lookups or on-disk for durability and large-scale use.
2. Similarity Search - Helps retrieve the vectors most similar to a query vector.
3. Indexing - Provide a data structure or method that enables fast similarity searches on
high-dimensional vectors (e.g., approximate nearest neighbor lookups).
4. CRUD Operations - Manage the lifecycle of data—adding new vectors, reading them,
updating existing entries, removing outdated vectors.

Use-cases
1. Semantic Search
2. RAG
3. Recommender Systems
4. Image/Multimedia search

# Vector Stores in LangChain
1. Supported Stores: LangChain integrates with multiple vector stores (FAISS, Pinecone, Chroma, Qdrant, Weaviate, etc.), giving you flexibility in scale, features, and deployment.
2. Common Interface: A uniform Vector Store API lets you swap out one backend (e.g., FAISS) for another (e.g., Pinecone) with minimal code changes.
3. Metadata Handling: Most vector stores in Lang Chain allow you to attach metadata (e.g., timestamps, authors) to each document, enabling filter-based retrieval.