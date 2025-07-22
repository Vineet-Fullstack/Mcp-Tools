from mcp.server.fastmcp import FastMCP

# Arithmetic tool functions

def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide the first number by the second. Raises error on division by zero."""
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
