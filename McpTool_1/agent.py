import os
from dotenv import load_dotenv

import asyncio
from google.adk.agents import Agent
from .agents.fs_agent import create_fs_agent
from .agents.web_surfing_agent import create_web_surfing_agent
from .agents.email_sender import create_email_agent




BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, './.env'))

# async def getMcpTool():
#     """Gets tools from the send email MCP server."""

#     tools,exit_stack = await MCPToolset.from_server(
#         connection_params=StdioServerParameters(
#             command="python",
#             args=[
#                 "/Users/princesingh/Documents/AgenticAI/GoogleADK/MCPADK/SendEmailMcpServ.py",
                
#             ],
#     )
#     )
#     return tools,exit_stack


async def create_root_agent():
    fs_agent,exit_stack = await create_fs_agent()
    web_surfing_agent,exit_stack = await create_web_surfing_agent()
    email_agent,exit_stack = await create_email_agent()
    

    agent = Agent(
        model="gemini-2.0-flash",
        name="root_assistant",
        description="General assistant taht tries to understand the user's needs and delegate tasks to sub agents",
        instruction="""
        You are a general assistant that tries to understand the user's needs , greet him and delegate tasks to sub agents.
        Here are the sub agents you can delegate tasks to:
        1. fs_agent: A file system agent that can perform file operations.
        2. web_surfing_agent: A web surfing agent that can perform web searches and retrieve information.
        3. email_agent: An email sender agent that can send emails.
        """,
        sub_agents=[
            fs_agent,
            web_surfing_agent,
            email_agent,
        ],
    )
    return agent, exit_stack




root_agent= create_root_agent()