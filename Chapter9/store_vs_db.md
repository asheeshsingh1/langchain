# Vector Store Vs Vector Database

## Vector Store
• Typically refers to a lightweight library or service that focuses on storing vectors (embeddings) and performing similarity search.
• May not include many traditional database features like transactions, rich query languages, or role-based access control.
• Ideal for prototyping, smaller-scale applications
• Examples FAISS (where you store vectors and can query them by similarity, but you handle persistence and scaling separately).

## Vector Database
• A full-fledged database system designed to store and query vectors.
• Offers additional "database-like" features:
• Distributed architecture for horizontal scaling
• Durability and persistence (replication, backup/restore)
• Metadata handling (schemas, filters)
• Potential for ACID or near-ACID guarantees
• Authentication/authorization and more advanced security
• Geared for production environments with significant scaling, large datasets
• Examples: Milvus, Qdrant, Weaviate. Pinccone

A vector database is effectively a vector store with extra database features (e.g., clustering, scaling, security, metadata filtering, and durability)
But vice versa is not true, not every vector store is a vector db.