from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Joke Tool Server")

@mcp.tool()
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return {"setup": joke["setup"], "punchline": joke["punchline"]}
    else:
        return {"error": "Failed to fetch joke"}

if __name__ == "__main__":
    mcp.run()
