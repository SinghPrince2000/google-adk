from google.adk.agents import Agent

from .fs_agent import create_fs_agent
from .web_surfing_agent import create_web_surfing_agent

async def create_root_agent():
    fs_agent,exit_stack = await create_fs_agent()
    web_surfing_agent,exit_stack = await create_web_surfing_agent()

    agent = Agent(
        model="gemini-2.0-flash",
        name="root_assistant",
        description="General assistant taht tries to understand the user's needs and delegate tasks to sub agents",
        instruction="""
        You are a general assistant that tries to understand the user's needs , greet him and delegate tasks to sub agents.
        Here are the sub agents you can delegate tasks to:
        1. fs_agent: A file system agent that can perform file operations.
        2. web_surfing_agent: A web surfing agent that can perform web searches and retrieve information.
        """,
        sub_agents=[
            fs_agent,
            web_surfing_agent
        ],
    )
    return agent, exit_stack

