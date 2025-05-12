import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from TripAdvisorSubAgents.tasks import  get_current_time,bidFarewell,showGreetings,calculate_sum
from TripAdvisorSubAgents.subAgents import greeting_agent, farewell_agent, calculation_agent,get_weather,get_Places,get_Hotels
from TripAdvisorSubAgents import prompt



async def create_agent():

    agent = Agent(
        name="TripAdvisorAgent",
        model="gemini-2.0-flash",
        description="The main coordinator agent.It delegates greetings/farewells to specialists and handles trip planning.",

        instruction=prompt.ROOT_AGENT_INSTR,                    

        tools=[get_weather,get_Places,get_Hotels,get_current_time],
        sub_agents=[
            greeting_agent,
            farewell_agent,
        ],
        output_key="trip_report",
    )
    return agent

root_agent = create_agent()

