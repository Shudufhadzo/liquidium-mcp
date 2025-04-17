from datetime import datetime, timezone
from typing import Any

from posthog_mcp.core import settings
from posthog_mcp.core.client import PostHogClient

client = PostHogClient()

async def create_annotation_request(
    project_id: int, 
    content: str, 
    date_marker: str | None = None
) -> dict[str, Any]:
    """Make a request to create a PostHog annotation."""
    data = {
        "content": content,
        "date_marker": date_marker or datetime.now(timezone.utc).isoformat()
    }
    
    return await client.post(
        settings.ANNOTATIONS_ENDPOINT.format(project_id=project_id),
        data=data
    )
