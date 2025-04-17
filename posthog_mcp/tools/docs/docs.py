from typing import Any

import httpx

from posthog_mcp.core import settings


async def search_docs(query: str) -> dict[str, Any]:
    """Search PostHog documentation using Inkeep."""
    if not settings.INKEEP_API_KEY:
        raise ValueError("INKEEP_API_KEY is required")

    headers = {
        "Authorization": f"Bearer {settings.INKEEP_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": settings.INKEEP_MODEL,
        "messages": [{"role": "user", "content": query}],
        "stream": False,
        "temperature": 0.7,
        "max_tokens": 1000
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{settings.INKEEP_BASE_URL}chat/completions",
                headers=headers,
                json=data,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}
