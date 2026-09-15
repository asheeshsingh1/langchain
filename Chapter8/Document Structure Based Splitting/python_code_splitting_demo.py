from langchain_classic.text_splitter import Language, RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=300, chunk_overlap=0
)

text = """
class Node:
def __init__(self,endpoint=None):
self.endpoint = endpoint
self.child = []
self.permission = {}
self.dynamic = None
class APIGateway:
def __init__(self):
self.root = Node("ROOT")
def load(self,req_method, req_path, perm_id):
parts = [part for part in req_path.split("/") if part]
curr = self.root
for part in parts:
if part.startswith("{") and part.endswith("}"):
if not curr.dynamic:
curr.dynamic = Node(part)
curr = curr.dynamic
else:
temp = None
for child in curr.child:
if child.endpoint == part:
temp = child
break
if not temp:
temp = Node(part)
curr.child.append(temp)
curr = temp
curr.permission[req_method] = perm_id
def search(self,req_method, req_path):
parts = [part for part in req_path.split("/") if part]
curr = self.root
for part in parts:
temp = None
for child in curr.child:
if child.endpoint == part:
temp = child
break
if not temp:
temp = curr.dynamic
if not temp:
return None
curr = temp
return curr.permission[req_method]
"""

res = splitter.split_text(text=text)

print(res[1])
