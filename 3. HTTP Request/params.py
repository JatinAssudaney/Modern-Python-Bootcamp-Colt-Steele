import requests
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat","limit": 1}
)
data = res.json()
print(data["results"])
