from mcp.server.fastmcp import FastMCP
import os
import sys

from posthog_mcp.tools.annotations.annotations import create_annotation_request
from posthog_mcp.tools.docs.docs import search_docs
from posthog_mcp.tools.insights.insights import get_insight_details, get_insights
from posthog_mcp.tools.projects.projects import get_current_organization, list_projects

# Initialize FastMCP server
mcp = FastMCP("liquidium")

@mcp.tool()
async def list_liquidium_projects() -> str:
    """List all available Liquidium projects."""
    org = await get_current_organization()
    if "error" in org:
        return f"Failed to get organization: {org['error']}"
    
    projects = await list_projects(org["id"])
    if "error" in projects:
        return f"Failed to list projects: {projects['error']}"
    
    if not projects:
        return "No projects found"
        
    return f"Available projects ({len(projects)}):\n" + "\n".join(
        f"ID: {p['id']} - Name: {p['name']}" for p in projects
    ) 

@mcp.tool()
async def create_liquidium_annotation(project_id: int, content: str, date_marker: str | None = None) -> str:
    """Create a Liquidium annotation.
    
    Args:
        project_id: The ID of the project as an integer (e.g. 99423)
        content: The content/text of the annotation
        date_marker: Optional ISO-8601 timestamp for the annotation (e.g. 2024-03-20T14:15:22Z)
    """
    result = await create_annotation_request(project_id, content, date_marker)
    
    if "error" in result:
        return f"Failed to create annotation: {result['error']}"
        
    return f"""Successfully created annotation:
ID: {result['id']}
Content: {result['content']}
Date: {result.get('date_marker', 'Now')}
Created by: {result['created_by']['email']}
""" 

@mcp.tool()
async def list_liquidium_insights(project_id: int, search: str | None = None) -> str:
    """List all available Liquidium insights for a project.
    
    Args:
        project_id: The ID of the project as an integer (e.g. 99423)
        search: Optional search query to filter insights
    """
    try:
        insights = await get_insights(project_id, search)
        
        if not insights:
            return "No insights found"
            
        formatted_insights = []
        for i in insights:
            insight_id = i.get('id') or i.get('short_id', 'N/A')
            name = i.get('name') or i.get('derived_name', 'Unnamed')
            formatted_insights.append(f"ID: {insight_id} - Name: {name}")
            
        return f"Available insights ({len(insights)}):\n" + "\n".join(formatted_insights)
    except Exception as e:
        return f"Failed to list insights: {str(e)}"

@mcp.tool()
async def search_liquidium_insights(project_id: int, search: str) -> str:
    """Search for Liquidium insights by name.
    
    Args:
        project_id: The ID of the project as an integer (e.g. 99423)
        search: The search query to filter insights by name
    """
    try:
        insights = await get_insights(project_id, search)
        
        if not insights:
            return "No insights found"
            
        formatted_insights = []
        for i in insights:
            insight_id = i.get('id') or i.get('short_id', 'N/A')
            name = i.get('name') or i.get('derived_name', 'Unnamed')
            formatted_insights.append(f"ID: {insight_id} - Name: {name}")
            
        return f"Search results ({len(insights)}):\n" + "\n".join(formatted_insights)
    except Exception as e:
        return f"Failed to search insights: {str(e)}"

@mcp.tool()
async def get_liquidium_insight_details(project_id: int, insight_id: int) -> str:
    """Get details for a specific Liquidium insight.
    
    Args:
        project_id: The ID of the project as an integer (e.g. 99423)
        insight_id: The ID of the insight as an integer (e.g. 12345)
    """
    try:
        insight_details = await get_insight_details(project_id, insight_id)
        
        if not insight_details:
            return "No insight details found"
            
        formatted_details = []
        for key, value in insight_details.items():
            formatted_details.append(f"{key}: {value}")
            
        return "Insight details:\n" + "\n".join(formatted_details)
    except Exception as e:
        return f"Failed to get insight details: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport='stdio')
