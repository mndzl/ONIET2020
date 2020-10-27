from django.shortcuts import render
import requests
import json
from datetime import *
from django.contrib.auth.decorators import login_required

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

    update_date = today["Date"]
    update_date = update_date[0:10]

    tenDaysAgo = respJson[0]
    newLast10Days = today["Confirmed"] - tenDaysAgo["Confirmed"] 
    context = {
        'total': today["Confirmed"],
        'recovered': today["Recovered"],
        'deaths': today["Deaths"],
        'update':update_date,
        'country': today["Country"],
        'new': newLast10Days,
    }
    return context

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
    
@login_required
def index(request):
    context = {}
    countries = getCountries()
    context = getData()

    return render(request, 'stats/index.html', context)
