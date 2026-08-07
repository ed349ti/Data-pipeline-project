import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "data.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "data_clean.csv")

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "database": "pipeline_db",
    "user": "postgres",
    "password": "postgres"
}
