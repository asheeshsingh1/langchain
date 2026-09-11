from langchain_community.document_loaders import WebBaseLoader

web_path = "https://en.wikipedia.org/wiki/Uttar_Pradesh_Legislative_Assembly"

loader = WebBaseLoader(web_path=web_path)

content = loader.load()
print(content)
