import requests
import json

url = 'https://api.covid19api.com/countries'
payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

res = response.json()

paises = []

for c in res:
    pais = c["Country"]
    paises.append(pais)

print(sorted(paises))
