from django.shortcuts import render
=======
import requests
import json
from datetime import *

def getData():
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
    newLast10Days = today["Confirmed"] - tenDaysAgo["Confirmed"] 
    context = {
        'total': today["Confirmed"],
        'recovered': today["Recovered"],
        'deaths': today["Deaths"],
        'update': today["Date"],
        'country': today["Country"],
        'new': newLast10Days,
    }
    return context
>>>>>>> 7aa248629d34adb814efb691c1271e7c31db1469

def getCountries():
    url = 'https://api.covid19api.com/countries'
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    res = response.json()

    countries = []

    for c in res:
        country = c["Country"]
        countries.append(country)
    
    return countries
    
def index(request):
    context = {}
    countries = getCountries()
    context = getData(context)

    return render(request, 'stats/index.html')
