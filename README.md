# Liquidium MCP Server 

A Model Context Protocol (MCP) server for interacting with PostHog analytics through Liquidium. Create annotations and manage projects directly through Claude Desktop or Smithery!

## Features 

- **List Projects**: View all available PostHog projects in your organization
- **Create Annotations**: Add annotations to your PostHog projects with optional timestamps
- **List and Search Insights**: View and search for insights in your PostHog projects
- **Get Insight Details**: View detailed information about specific insights

## Setup 

### Option 1: Smithery (Recommended)

The easiest way to use Liquidium MCP is through Smithery:

1. Visit [Liquidium MCP on Smithery](https://smithery.ai/servers/liquidium-mcp)
2. Click "Add to Claude"
3. Enter your PostHog API Key when prompted
4. Start using Liquidium tools in Claude!

### Option 2: Local Installation

1. **Prerequisites**

   - Python 3.10 or higher
   - `pip` or `uv` package manager
   - PostHog API Key with `annotation:write` and `project:read` scopes obtained from your [project settings](https://app.posthog.com/project/settings)

2. **Installation**

   ```bash
   # clone the repo
   git clone https://github.com/Shudufhadzo/liquidium-mcp.git

   cd liquidium-mcp

   # Create and activate virtual environment
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate

   # Install dependencies
   pip install -e .
   ```

3. **Configuration**

   - Create a `.env` file in the project root:
     ```
     PERSONAL_API_KEY=phx_your_posthog_api_key_here
     ```

4. **Claude Desktop Setup**
   - Install [Claude Desktop](https://claude.ai/desktop)
   - Open Claude Desktop settings and click "Edit Config". Alternatively, you can open the file from:
     - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
     - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Add this to your `claude_desktop_config.json` (adjust paths according to your system):
     ```json
     {
       "mcpServers": {
         "posthog": {
           "command": "/path/to/python",  # Get this by running: which python
           "args": [
             "-m",
             "posthog_mcp",
             "--directory",
             "/path/to/your/posthog-mcp"  # Full path to this project
           ]
         }
       }
     }
     ```
     Check [the latest documentation](https://modelcontextprotocol.io/quickstart/user) on setting up Claude Desktop as MCP client if you ran into any issues.

## Usage 

After setup, you'll see a hammer  icon in Claude Desktop. The following commands are available:

### List Projects

Ask Claude:

```
"List my PostHog projects"
```

### Get and Search for Insights

Ask Claude:

"List my PostHog insights" or "Search for revenue insights in my PostHog"

### Search for documentations online

You can ask:

- "how can i do reverse proxy in nextjs in posthog?"

### Create Annotation

Using the Project ID you get from the list of projects, ask Claude:

```
"Create a PostHog annotation in project 53497 saying 'Deployed v1.2.3'"

```

or with a specific date:

```
"Create a PostHog annotation in project 53497 for March 20th saying 'Started new marketing campaign'"
```

## Troubleshooting 

- If the hammer icon doesn't appear, restart Claude Desktop
- Check logs at `~/Library/Logs/Claude/mcp*.log` (macOS) or `%APPDATA%\Claude\logs` (Windows)
- Verify your PostHog API key has the correct permissions
- Make sure all paths in `claude_desktop_config.json` are absolute paths

## Contributing 

Feel free to open issues and PRs! We follow PostHog's contribution guidelines.
