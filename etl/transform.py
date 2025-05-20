from config.logger import get_logger

logger = get_logger(__name__)

def transform_repo_data(raw_data):
    logger.info("Transforming data...")
    transformed = []
    for repo in raw_data:
        transformed.append({
            "id": repo["id"],
             "full_name": repo["full_name"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "stargazers_count": repo["stargazers_count"],
            "language": repo["language"],
            "created_at": repo["created_at"]
        })
    return transformed;