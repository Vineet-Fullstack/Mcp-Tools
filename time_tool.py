from mcp.server.fastmcp import FastMCP
import datetime

mcp = FastMCP("Time Tool Server")

@mcp.tool()
def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    mcp.run()
