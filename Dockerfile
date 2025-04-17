FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy the entire application
COPY . .

# Install Python dependencies and the package
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .

# Run the MCP server
CMD ["python", "-m", "posthog_mcp"]
