import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "api/analyze_list", json={"tickers": ["AMZN", "NYCB", "META"]})
print(response.json())
