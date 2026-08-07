from src.extract import extract_from_api
from src.transform import transform
from src.load import load

def run_pipeline():
    print("🚀 Iniciando pipeline...")

    df = extract_from_api()
    df_transformed = transform(df)
    load(df_transformed)

    print("✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()
