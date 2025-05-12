from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams, StdioServerParameters

async def get_web_surfing_mcp_tools_async():
    """Gets tools from the web surfing MCP Server."""

    tools,exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command="npx",
            args=["-y","puppeteer-mcp-server"],

        )
    )
    return tools,exit_stack