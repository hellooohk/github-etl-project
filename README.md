# 🚀 GitHub Repositories ETL Pipeline

A modular ETL (Extract, Transform, Load) pipeline that fetches top GitHub repositories based on a topic, processes the data, and stores it into a local SQLite database. Built with best industry practices in mind.

---

## 🛠 Tech Stack

| Purpose         | Tool                      |
|-----------------|---------------------------|
| Language        | Python 3.x                |
| Data Extraction | GitHub REST API           |
| Data Storage    | SQLite                    |
| Config & Secrets| `.env` + `dotenv`         |
| Logging         | `logging` + `colorama`    |
| Structure       | Modular Python packages   |

---

## 📁 Project Structure

```

github\_etl\_project/
├── etl/
│   ├── extract.py         # Extracts data from GitHub API
│   ├── transform.py       # Cleans and transforms raw data
│   └── load.py            # Loads cleaned data into SQLite
│
├── config/
│   ├── settings.py        # Configuration and constants
│   └── logger.py          # Colorful and file-based logging setup
│
├── db/
│   └── schema.sql         # (Optional) SQL schema if needed
│
├── logs/
│   └── run.log            # Log file (auto-generated)
│
├── main.py                # Entrypoint to run the ETL job
├── .env                   # Secrets and environment variables
├── requirements.txt       # Python dependencies
└── README.md              # Project overview

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/github-etl-project.git
cd github-etl-project
````

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root:

```env
TOPIC=data engineering
```

You can change `TOPIC` to anything like `"react"`, `"machine learning"`, etc.

---

## 🚀 Running the ETL Pipeline

```bash
python main.py
```

This will:

* Extract top 10 repositories from GitHub for the given topic
* Transform the data into clean structure
* Load it into a local SQLite database `db/github_repos.db`
* Log the whole process to `logs/run.log` and terminal (with colors!)

---

## 📊 Example Output

**Database (`db/github_repos.db`)**

| id       | full\_name     | stars | language   |
| -------- | -------------- | ----- | ---------- |
| 28457823 | facebook/react | 220k  | JavaScript |
| ...      | ...            | ...   | ...        |

**Log (`logs/run.log`)**

```
2025-05-20 13:21:10 - INFO - ETL job started.
2025-05-20 13:21:11 - INFO - Fetching from GitHub API...
2025-05-20 13:21:12 - INFO - Loading to DB...
2025-05-20 13:21:13 - INFO - ETL job completed.
```

---

## ✅ Best Practices Used

* 🧱 Modular Code (`extract`, `transform`, `load`)
* 🔐 Config via `.env`
* 🖥 Logs to both terminal and file
* 🎨 Colored CLI logs for easier debugging
* 📦 Ready for Docker, Airflow, or cron extension
* 🧪 Easily testable functions

---

## 📌 Next Steps (Optional Enhancements)

* [ ] Add unit tests with `pytest`
* [ ] Switch to PostgreSQL or cloud database
* [ ] Schedule with Airflow or Prefect
* [ ] Dockerize the pipeline
* [ ] Add retry and exponential backoff to API calls

---

## 📄 License

MIT License. Free to use, share, and learn from.
