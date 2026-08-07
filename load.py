import pandas as pd
from sqlalchemy import create_engine
from config import PROCESSED_DATA_PATH, DB_CONFIG

def save_to_csv(df):
    print("💾 Salvando CSV processado...")
    df.to_csv(PROCESSED_DATA_PATH, index=False)

def save_to_postgres(df):
    print("🐘 Salvando no PostgreSQL...")

    connection_string = (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

    engine = create_engine(connection_string)

    df.to_sql("dados_pipeline", engine, if_exists="replace", index=False)

def load(df):
    save_to_csv(df)
    save_to_postgres(df)
