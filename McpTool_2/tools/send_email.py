from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams, StdioServerParameters

async def email_sender():

    """Gets tools from the  MCP Server."""

    tools,exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command="python",
            args=[
                "/Users/princesingh/Documents/AgenticAI/GoogleADK/MCPADK/SendEmailMcpServ.py",
                
            ],
    )
    )
    return tools,exit_stack