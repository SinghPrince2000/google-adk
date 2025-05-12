
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams, StdioServerParameters

from google.adk.tools.google_search_tool import google_search






def showGreetings(name:str) -> dict:
    """Returns a greeting message for the specified name.
    Args:
        name (str): The name of the person to greet.
   
    Returns:
        dict: status and result or error msg.
    """
   
    greeting = f"Hello, {name}! How can I assist you today?"
    return {"status": "success", "report": greeting}


def calculate_sum(a:int, b:int) -> dict:
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        dict: status and result or error msg.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return {
            "status": "error",
            "error_message": "Both inputs must be numbers.",
        }
    
    result = a + b
    return {"status": "success", "result": result}

def bidFarewell() -> dict:
    """Returns a farewell message .
    
    Returns:
        dict: status and result .
    """
    
    farewell = f"Goodbye,! Have a great day!"
    return {"status": "success", "report": farewell}

# def get_weather(city: str) -> dict:
#     """Retrieves the current weather report for a specified city.

#     Args:
#         city (str): The name of the city for which to retrieve the weather report.

#     Returns:
#         dict: status and result or error msg.
#     """
#     if city.lower() == "new york":
#         return {
#             "status": "success",
#             "report": (
#                 "The weather in New York is sunny with a temperature of 25 degrees"
#                 " Celsius (41 degrees Fahrenheit)."
#             ),
#         }
#     else:
#         return {
#             "status": "error",
#             "error_message": f"Weather information for '{city}' is not available.",
#         }

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}




async def getMcpTool():
    """Gets tools from the send email MCP server."""

    tools,exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command="python",
            args=[
                "/Users/princesingh/Documents/AgenticAI/GoogleADK/MCPADK/SendEmailMcpServ.py",
                
            ],
    )
    )
    return tools,exit_stack

# def send_email(recipient_email:str ,travel_plan:str)-> dict:
#     """
#     Sends an email using SMTP.
#     This function creates an email message, connects to the Gmail SMTP server,
#     Args:
#         recipient_email (str): The recipient's email address.
#         travel_plan (str): The travel plan to be included in the email body.
#     Returns:
#         dict: Status of the email sending process.
#     """
#     try:
#         # Create the email
#         msg = MIMEMultipart()
#         msg['From'] = 'singh24prince.2000@gmail.com'
#         msg['To'] = recipient_email
#         msg['Subject'] = ' Travel Plan'
#         msg.attach(MIMEText(travel_plan, 'plain'))

#         # Connect to the SMTP server
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()  # Upgrade the connection to secure
#             server.login('singh24prince.2000@gmail.com', 'kbfijsipnbvdoymw')  # Log in to the server
#             server.send_message(msg)  # Send the email

#         return {"status": "success", "message": "Email sent successfully."}
#     except Exception as e:
#         return {"status": "error", "error_message": str(e)}



def print_output(output:str)-> dict:
    """
    Prints the output to the console.
    Args:
        output (str): The output to be printed.
    Returns:
        dict: Status of the print operation.
    """
    print(output)
    return {"status": "success", "message": "Output printed successfully."}