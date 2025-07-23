# pip install mcp[cli]
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather_server")

# Defining constants
WEATHER_API_BASE = "https://wttr.in"
USER_AGENT = "weather-mcp-server/1.0"


# Defining the MCP tools
@mcp.tool()
def get_weather_info(location: str) -> str:
    """Get Weather information for a given location.

    Args:
        location (str):
            The location for which to get the weather information.
            The location needs to be a proper city name like London, Tokyo etc.
    """
    url = f"{WEATHER_API_BASE}/{location}?format=j1"

    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    return str(response.json())


if __name__ == "__main__":
    # Initialize and start the MCP server
    mcp.run()
