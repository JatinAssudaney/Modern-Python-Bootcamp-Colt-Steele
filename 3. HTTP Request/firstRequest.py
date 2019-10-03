import requests

url = "www.google.com"
res = requests.get(url)

print(res.text)
