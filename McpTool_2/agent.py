import os
from dotenv import load_dotenv

import asyncio
from google.adk.agents import Agent
from .agents.fs_agent import create_fs_agent
from .agents.web_surfing_agent import create_web_surfing_agent
from .agents.email_sender import create_email_agent
from .tools.send_email import email_sender
from google.adk.tools.base_tool import BaseTool




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
    send_email,exit_stack = await email_sender()

     # Ensure send_email_tool is callable or an instance of BaseTool
    if not callable(send_email) and not isinstance(send_email, BaseTool):
        raise TypeError(
            f"send_email_tool must be callable or an instance of BaseTool. Got: {type(send_email)}"
        )
    
    print(type(send_email))
    agent = Agent(
        model="gemini-2.0-flash",
        name="root_assistant",
        description="General assistant taht tries to understand the user's needs and delegate tasks to sub agents",
        instruction="""
        You are a general assistant that tries to understand the user's needs , greet him and delegate tasks to sub agents.

        you have access to following sub agents:
        1. fs_agent: You can use this agent to read and write files, and perform file system operations.
        2. web_surfing_agent: You can use this agent to search the web and get information from the internet.
        3. email_agent: You can use this agent to send emails to the user or other people.
        
        """,
        
       sub_agents=[
            fs_agent,
            web_surfing_agent,
            email_agent,
        ],
    )
    return agent, exit_stack




root_agent= create_root_agent()