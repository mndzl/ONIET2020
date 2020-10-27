import requests
import json
from datetime import *

today = date.today()
dateFrom = today - timedelta(days=10)

url = "https://api.covid19api.com/country/argentina"

parameters = {
    "from": dateFrom,
    "to": today,
}

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, params=parameters)

respJson = response.json()
today = respJson[-1]
tenDaysAgo = respJson[0]
countryTotal = today["Confirmed"]
countryRecovered = today["Recovered"]
countryDeaths = today["Deaths"]
countryActive = today["Active"]
lastUpdate = today["Date"]
newLast10Days = today["Confirmed"] - tenDaysAgo["Confirmed"] 


