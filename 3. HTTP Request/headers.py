import requests
url = "https://icanhazdadjoke.com/"
# res = requests.get(url, headers={"Accept": "text/plain"})
# print(res.text)
res = requests.get(url, headers={"Accept": "application/json"})
# Dictionary Will be Returned
data = res.json()
print(data["joke"])
