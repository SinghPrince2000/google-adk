from google.adk.agents import Agent
from ..tools.fs_mcp import get_fs_mcp_tools_async

async def create_fs_agent():
    fs_tools,exit_stack = await get_fs_mcp_tools_async()
    print("type of fs tool",type(fs_tools))
    agent = Agent(
        model="gemini-2.0-flash",
        name="fs_agent",
        description="A file system agent that can perform file operations.",
        instruction="""
        You are a file system agent that can perform file operations.
        Here are the tools you can use:
        1. fs_tools: A tool that can perform file operations.
        """,
        tools=fs_tools,
    )
    return agent, exit_stack