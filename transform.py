import pandas as pd

def clean_data(df):
    print("🧹 Limpando dados...")

    # remover duplicados
    df = df.drop_duplicates()

    # tratar valores nulos
    df = df.fillna("N/A")

    return df

def feature_engineering(df):
    print("🧠 Criando novas features...")

    if "title" in df.columns:
        df["title_length"] = df["title"].apply(len)

    return df

def transform(df):
    df = clean_data(df)
    df = feature_engineering(df)
    
    return df
