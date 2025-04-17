FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY pyproject.toml ./

# Install uv for package management
RUN pip install --no-cache-dir uv

# Copy the rest of the application
COPY . .

# Install the package
RUN uv pip install .

# Run the MCP server
CMD ["python", "-m", "posthog_mcp"]
