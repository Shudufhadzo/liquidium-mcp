from typing import Any, List

from posthog_mcp.core import settings
from posthog_mcp.core.client import PostHogClient

client = PostHogClient()

async def get_insights(project_id: int, search: str | None = None) -> List[dict[str, Any]]:
    """Get insights for a project.
    
    Args:
        project_id: The ID of the project
        search: Optional search query to filter insights
    """
    endpoint = settings.INSIGHTS_ENDPOINT.format(project_id=project_id)
    params = ["limit=10"]
    
    if search:
        params.append(f"search={search}")
    
    if params:
        endpoint += "?" + "&".join(params)
        
    response = await client.get(endpoint)
    
    # Handle error response from client
    if isinstance(response, dict) and "error" in response:
        raise Exception(response["error"])
        
    # Handle paginated response format
    if isinstance(response, dict) and "results" in response:
        return response["results"]
        
    return []


async def get_insight_details(project_id: int, insight_id: int) -> dict[str, Any]:
    """Get details for an insight."""
    return await client.get(settings.INSIGHT_DETAILS_ENDPOINT.format(project_id=project_id, insight_id=insight_id))

