from config.logger import get_logger
from etl.extract import fetch_github_repos
from etl.transform import transform_repo_data
from etl.load import init_db, load_to_db

logger = get_logger(__name__)


def main():
    logger.info("ETL process started.")
    init_db()
    raw_data = fetch_github_repos()
    transformed_data = transform_repo_data(raw_data)
    load_to_db(transformed_data)
    logger.info("ETL process completed.")


if __name__ == "__main__":
    main()
