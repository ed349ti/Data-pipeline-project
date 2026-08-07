import pandas as pd
import requests
from config import RAW_DATA_PATH

def extract_from_csv():
    print("📥 Extraindo dados de CSV...")
    df = pd.read_csv(RAW_DATA_PATH)
    return df

def extract_from_api():
    print("🌐 Extraindo dados de API...")
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        raise Exception("Erro ao acessar API")

if __name__ == "__main__":
    df = extract_from_api()
    print(df.head())
