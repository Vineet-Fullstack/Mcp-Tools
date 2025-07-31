import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name=os.environ.get("MCP_SERVER_NAME", "Payrix API"))
