from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams, StdioServerParameters

async def get_fs_mcp_tools_async():
    """Gets tools from the LinkedIn Navigator MCP server."""

    tools,exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "/Users/princesingh/Documents"
            ]
    )
    )
    return tools,exit_stack