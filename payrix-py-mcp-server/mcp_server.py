#!/usr/bin/env python3
"""
MCP Server Implementation for Payrix

This MCP server exposes the API operations defined in the OpenAPI specification
as MCP tools and resources.
"""

import os
import argparse
import logging
import httpx
from typing import Dict, List, Any, Optional, Union
from mcp.server.fastmcp import FastMCP, Context
from mcp_tools import *
from mcp_resources import *
from mcp_prompts import *
from mcp_instance import mcp

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="MCP Server for Payrix")
    parser.add_argument(
        "--transport", 
        choices=["sse", "io"], 
        default="sse",
        help="Transport type (sse or io)"
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    logger.info(f"Starting MCP server with {args.transport} transport")
    
    if args.transport == "sse":
        # Run with SSE transport (default host and port)
        mcp.run(transport="sse")
    else:
        # Run with stdio transport
        mcp.run(transport="stdio")