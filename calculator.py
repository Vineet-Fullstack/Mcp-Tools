from mcp.server.fastmcp import FastMCP  # Import FastMCP, the quickstart server base
from tools.arithmetic import add, subtract, multiply, divide  # Import arithmetic functions from tools.arithmetic

mcp = FastMCP("Calculator Server")  # Initialize an MCP server instance with a descriptive name

@mcp.tool()  # Register a function as a callable tool for the model
def add_tool(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return add(a, b)  # Simple arithmetic logic

@mcp.tool()
def subtract_tool(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    return subtract(a, b)

@mcp.tool()
def multiply_tool(a: int, b: int) -> int:
    """Multiply two numbers."""
    return multiply(a, b)

@mcp.tool()
def divide_tool(a: float, b: float) -> float:
    """Divide the first number by the second. Raises error on division by zero."""
    if b == 0:
        raise ValueError("Division by zero")
    return divide(a, b)
    
if __name__ == "__main__":
    mcp.run(transport="stdio")  # Run the server, using standard input/output for communication