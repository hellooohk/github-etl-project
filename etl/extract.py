import requests
from config.settings import GITHUB_API_URL
from config.logger import get_logger

logger = get_logger(__name__)
def fetch_github_repos():
    logger.info("Fetching data from GitHub API")
    response = requests.get(GITHUB_API_URL)
    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")
    return response.json()["items"]