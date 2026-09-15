from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke("top news in india today")

print(results)
print(search_tool.name)
print(search_tool.description)
print(search_tool.args)

shell_tool = ShellTool()

results = shell_tool.invoke("ls")

print(results)
