import os
from typing import Literal

from dotenv import load_dotenv

# Only load from .env if not already set in environment
if not os.getenv("PERSONAL_API_KEY"):
    load_dotenv(verbose=False)

REGION_ENDPOINTS = {
    "us": "https://us.posthog.com",
    "eu": "https://eu.posthog.com"
}

PERSONAL_API_KEY = os.getenv("PERSONAL_API_KEY")
POSTHOG_REGION: Literal["us", "eu"] = os.getenv("POSTHOG_REGION", "us")
API_ENDPOINT = REGION_ENDPOINTS[POSTHOG_REGION]


# API Endpoints
CURRENT_ORG_ENDPOINT = "/api/organizations/@current/"
PROJECTS_ENDPOINT = "/api/organizations/{org_id}/projects/"
ANNOTATIONS_ENDPOINT = "/api/projects/{project_id}/annotations/" 
INSIGHTS_ENDPOINT = "/api/projects/{project_id}/insights/"
INSIGHT_DETAILS_ENDPOINT = "/api/projects/{project_id}/insights/{insight_id}/"

# Inkeep settings
INKEEP_API_KEY = os.getenv("INKEEP_API_KEY")
INKEEP_BASE_URL = os.getenv("INKEEP_BASE_URL", "https://api.inkeep.com/v1/")
INKEEP_MODEL = os.getenv("INKEEP_MODEL", "inkeep-qa-expert")
