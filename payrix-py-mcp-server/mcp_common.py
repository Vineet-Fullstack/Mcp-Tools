import os
import httpx

# API configuration (import or redefine as needed)
API_URL = os.environ.get("API_URL", "")
API_TOKEN = os.environ.get("API_TOKEN", "")

async def get_http_client():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "APIKey": API_TOKEN
    }
    return httpx.AsyncClient(
        base_url=API_URL,
        headers=headers
    )
