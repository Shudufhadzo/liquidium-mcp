from typing import Any, List

from posthog_mcp.core import settings
from posthog_mcp.core.client import PostHogClient

client = PostHogClient()

async def get_current_organization() -> dict[str, Any]:
    """Get current organization details."""
    return await client.get(settings.CURRENT_ORG_ENDPOINT)

async def list_projects(org_id: str) -> List[dict[str, Any]]:
    """List all projects in an organization."""
    data = await client.get(settings.PROJECTS_ENDPOINT.format(org_id=org_id))
    return data.get("results", []) if "results" in data else []

