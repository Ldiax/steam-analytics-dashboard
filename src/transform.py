import pandas as pd
import json

def load_raw_data(path="data/raw/games_raw.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def clean_owners(df):
    def parse_owners(value):
        parts = value.split('..')
        low = int(parts[0].replace(',', '').strip())
        high = int(parts[1].replace(',', '').strip())
        return (low + high) / 2

    df["owners"] = df["owners"].apply(parse_owners)
    return df

def clean_prices(df):
    df["price"] = df["price"].astype(float)
    df["initialprice"] = df["initialprice"].astype(float)
    df["discount"] = df["discount"].astype(float)
    return df

def clean_playtime(df):
    df["average_forever"] = df["average_forever"] / 60
    return df

def add_features(df):
    df["rating_score"] = df["positive"] / (df["positive"] + df["negative"]) * 100
    df["revenue_estimate"] = (df["owners"] * df["price"]) / 100
    return df

def clean_data(df):
    df = clean_owners(df)
    df = clean_prices(df)
    df = clean_playtime(df)
    df = add_features(df)
    return df

def main():
    df = load_raw_data()
    df = clean_data(df)
    print(df.dtypes)
    print(df.head())

if __name__ == "__main__":
    main()