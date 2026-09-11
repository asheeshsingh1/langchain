from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./Chapter7/Docs/ML.pdf")

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)
