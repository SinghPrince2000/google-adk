from google.adk.agents import Agent
from ..tools.send_email import email_sender

async def create_email_agent():
    tools,exit_stack = await email_sender()
    agent = Agent(
        model="gemini-2.0-flash",
        name="email_sender",
        description="Handles email sending.",
        instruction="""
        You are a email sender agent that can send email using the tools.
        """,
        tools=tools,
    )
    return agent, exit_stack