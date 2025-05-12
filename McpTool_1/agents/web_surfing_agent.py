from google.adk.agents import Agent
from ..tools.web_surfing_mcp import get_web_surfing_mcp_tools_async

async def create_web_surfing_agent():
    web_surfing_tools, exit_stack = await get_web_surfing_mcp_tools_async()
    agent = Agent(
        model="gemini-2.0-flash",
        name="web_surfing_agent",
        description="A web surfing agent that can perform web searches and retrieve information.",
        instruction="""
        You are a web surfing agent that can perform web searches and retrieve information.
        Here are the tools you can use:
        1. web_surfing_tools: A tool that can perform web searches and retrieve information.
        """,
        tools=web_surfing_tools,
    )
    return agent, exit_stack