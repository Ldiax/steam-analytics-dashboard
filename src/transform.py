import pandas as pd
import json

with open("data/raw/games_raw.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

def clean_data(df):
    
    # 2. price, initialprice, discount: converter para float
    # 3. average_forever: converter de minutos para horas
    return df