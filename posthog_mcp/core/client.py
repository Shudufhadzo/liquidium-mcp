from datetime import datetime, timezone
from typing import Any
from urllib.parse import urljoin

import httpx

from posthog_mcp.core import settings


class PostHogClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or settings.PERSONAL_API_KEY
        self.base_url = settings.API_ENDPOINT
        self.headers = {}
        
        if self.api_key:
            self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
    async def get(self, endpoint: str) -> dict[str, Any]:
        """Make a GET request to the API."""
        if not self.api_key:
            return {"error": "API key is required"}
        return await self._make_request("GET", endpoint)
        
    async def post(self, endpoint: str, data: dict | None = None) -> dict[str, Any]:
        """Make a POST request to the API."""
        if not self.api_key:
            return {"error": "API key is required"}
        return await self._make_request("POST", endpoint, data)
        
    async def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        data: dict | None = None
    ) -> dict[str, Any]:
        url = urljoin(self.base_url, endpoint)
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=self.headers,
                    json=data,
                    timeout=30.0
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                return {"error": str(e)}

    async def get_current_organization(self) -> dict[str, Any]:
        """Get current organization details."""
        if not self.api_key:
            return {"error": "API key is required"}
        return await self._make_request("GET", settings.CURRENT_ORG_ENDPOINT)

    async def list_projects(self, org_id: str) -> dict[str, Any]:
        """List all projects in an organization."""
        if not self.api_key:
            return {"error": "API key is required"}
        return await self._make_request(
            "GET", 
            settings.PROJECTS_ENDPOINT.format(org_id=org_id)
        )

    async def create_annotation(
        self, 
        project_id: int, 
        content: str, 
        date_marker: str | None = None
    ) -> dict[str, Any]:
        """Create a new annotation."""
        if not self.api_key:
            return {"error": "API key is required"}
        data = {
            "content": content,
            "date_marker": date_marker or datetime.now(timezone.utc).isoformat()
        }
        
        return await self._make_request(
            "POST",
            settings.ANNOTATIONS_ENDPOINT.format(project_id=project_id),
            data=data
        )