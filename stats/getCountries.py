import requests
import json

url = 'https://api.covid19api.com/countries'
payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

res = response.json()

#def jprint(obj):
#    text = json.dumps(obj, sort_keys=True,indent=4)
#    print(text)
#jprint(res)

paises = []

for c in res:
    pais = c["Country"]
    paises.append(pais)

print(paises)



# print(response.text.encode('utf8'))