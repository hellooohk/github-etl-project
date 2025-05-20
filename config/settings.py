import os
from dotenv import load_dotenv

load_dotenv()

TOPIC = os.getenv("TOPIC", "data engineering")
GITHUB_API_URL = f"https://api.github.com/search/repositories?q={TOPIC}&sort=stars&order=desc&per_page=10"
DATABASE = "db/github_repos.db"