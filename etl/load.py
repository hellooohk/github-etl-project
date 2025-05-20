import sqlite3
from config.logger import get_logger
from config.settings import DATABASE

logger = get_logger(__name__)

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repositories (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            html_url TEXT,
            description TEXT,
            stargazers_count INTEGER,
            language TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def load_to_db(data):
    logger.info("Loading data into the database...")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    for repo in data:
        cursor.execute("""
            INSERT OR IGNORE INTO repositories 
            (id, full_name, html_url, description, stargazers_count, language, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, tuple(repo.values()))
    conn.commit()
    conn.close()