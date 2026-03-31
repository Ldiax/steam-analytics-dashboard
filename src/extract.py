import requests
import json

def get_top_games():
    url = "https://steamspy.com/api.php?request=top100in2weeks"
    response = requests.get(url)
    data = response.json()
    return list(data.values())

def save_raw_data(data, path="data/raw/games_raw.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{len(data)} jogos salvos em {path}")

if __name__ == "__main__":
    games = get_top_games()
    save_raw_data(games)