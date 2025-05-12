from TripAdvisorSubAgents.tasks import  get_current_time, bidFarewell, showGreetings, calculate_sum,print_output
from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from .tasks import getMcpTool


greeting_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Handles simple greetings.",
    instruction="You are a greeting agent. Your task is to respond to simple greetings like 'Hi Prince ', 'Hello Rahul'.If Name is not provided, respond with a generic greeting and ask for the name.",
    tools=[showGreetings],
)
farewell_agent = Agent(
    name="farewell_agent",
    model="gemini-2.0-flash",
    description="Handles simple farewells.",
    instruction="You are a farewell agent. Your task is to respond to simple farewells like 'Bye', 'See you'.",
    tools=[bidFarewell],
)
calculation_agent = Agent(
    name="calculation_agent",
    model="gemini-2.0-flash",
    description="Handles simple calculations.",
    instruction="You are a calculation agent. Your task is to respond to simple calculations like 'sum of 2 and 3'.",
    tools=[calculate_sum],
)



"""Wrapper to Google Search Grounding with custom prompt."""
Weather_agent = Agent(
    name="Weather_agent",
    model="gemini-2.0-flash",
    description="Handles Weather request for planning trip to requested places and suggests better nearby places based on weather condtions.",
    instruction=""" Answer the user's question directly using google_search grounding tool; Provide a brief but concise response. 
    Rather than a detail response, provide the current weather situation *strictly* following the step in <WEATHER_STEPS/> block .

    <WEATHER_STEPS>
        1. Get the current weather in the destination city using 'google_search' tool.
        2. Evaluate the weather conditions based on <CRITERIA/> .
        3. If the weather is good, provide a list of items to pack for the trip.
        4. If the weather is bad, *strictly* Use 'google_search' tool to suggest the list of alternate nearby cities with 'good weather' conditions using <CRITERIA/> block  and their weather report .
        5. If weather is bad ,*alternate cities* should have 'good weather' conditions as per  <CRITERIA/> block.
    </WEATHER_STEPS>
    
    <CRITERIA>
        *If* Temperature is more than 35 degrees Celsius.
            *then* weather is bad.
        *If* Temperature is less than 0 degrees Celsius.
            *then* weather is bad.
        *If* It is raining.
            *then* weather is bad.
        *else* weather is good.
    </CRITERIA>
   
    Do not ask the user to check or look up information for themselves, that's your role; do your best to be informative.
    
    """,
    tools=[google_search],
    output_key="weather_report",
)
get_Places = Agent(
    name="get_Places",
    model="gemini-2.0-flash",
    description="Get list of places to visit in the city based on the weather.",
    instruction="""
    Answer the user's question directly using google_search grounding tool ;
    Parse the city with 'good weather' from the weather report provided in session key 'weather_report' to get idea of places to visit;

   
   
     Provide a brief but concise response.
   
    Do not ask the user to check or look up information for themselves, that's your role; do your best to be informative.
    """,
    tools=[google_search],
    output_key="places_report",
)

get_Hotels = Agent(
    name="get_Hotels",
    model="gemini-2.0-flash",
    description="Get list of hotels in the city.",
    instruction="""
    Answer the user's question directly using google_search grounding tool ;

    Strictly Use the destination provided in places report provided in session key 'places_report' to get idea of places to visit;;
    
   

     Provide a brief but concise response.
    
    Do not ask the user to check or look up information for themselves, that's your role; do your best to be informative.
    Please ignore queries other than hotel search to get the list of hotels in the city;
    """,
    tools=[google_search],
    output_key="hotels_report",
)


async def create_email_sender():
    tools, exit_stack = await getMcpTool()

    email_sender = Agent(
        name="email_sender",
        model="gemini-2.0-flash",
        description="Handles email sending.",
        instruction="You are a email sender agent. Your task is to send an email.",
        tools=tools,
    )

    return email_sender, exit_stack


get_weather = AgentTool(agent=Weather_agent)
get_Places = AgentTool(agent=get_Places)
get_Hotels = AgentTool(agent=get_Hotels)




