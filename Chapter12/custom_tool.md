# Custom Tool

## Ways to create custom tools:
- Use @tool decorator
- Use StructuredTool and Pydantic
- Use BaseTool class

## Toolkit
A toolkit is just a collection (bundle) of related tools that serve a common purpose - packaged together for convenience and reusability.

In LangChain:
- A toolkit might be: GoogleDriveToolkit.
- And it can contain the following tools.

* GoogleDriveCreateFileTool : Upload a file
* GoogleDriveSearchTool : Search for a file by name/content
* GoogleDriveReadFileTool: Read contents of a file