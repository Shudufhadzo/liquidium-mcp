"""PostHog MCP tools for annotations and project management."""
from . import server

__version__ = "0.1.0"

def main():
    """Main entry point for the package."""
    server.mcp.run(transport='stdio')

__all__ = ["server", "main"]
