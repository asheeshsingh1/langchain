# What are Retrievers
- A retriever is a component in LangChain that fetches relevant documents from a
data source in response to a user’s query.
- There are multiple types of retrievers
- All retrievers in LangChain are runnables.

## Data Source based classification of Retrievers
- Wikipedia Retriever
- Vector Store Retriever
- Arxiv Retriever

## Search Startegy based classification of Retrievers
- MMR Retriever
- Multi Query Retriever
- Contextual Comparision Retriever

### Wikipedia Retriever
A Wikipedia Retriever is a retriever that queries the Wikipedia API to fetch relevant content for a given query.

How it works:
1. You give it a query (e.g., "Albert Einstein")
2. It sends the query to Wikipedia's API
3. It retrieves the most relevant articles
4. It returns them as LangChain Document objects

### Vector Store Retriever
A Vector Store Retriever in LangChain is the most common type of retriever that
lets you search and fetch documents from a vector store based on semantic similarity using vector embeddings.

How It Works:
1. You store your documents in a vector store (like FAISS, Chroma, Weaviate)
2. Each document is converted into a dense vector using an embedding model
3. When the user enters a query:
    - It's also turned into a vector.
    - The retriever compares the query vector with the stored vectors.
    - It retrieves the top-k most similar ones.


### Maximal Marginal Relevance (MMR)
How can we pick results that are not only relevant to the query but also different from each other?
- MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query.

Why MMR Retriever?
- In regular similarity search, you may get documents that are:
    - All very similar to each other.
    - Repeating the same info.
    - Lacking diverse perspectives.

MMR Retriever avoids that by:
- Picking the most relevant document first.
- Then picking the next most relevant and least similar to already selected docs.

This helps especially in RAG pipelines where:
- You want your context window to contain diverse but still relevant information.
- Especially useful when documents are semantically overlapping.