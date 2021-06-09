from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    data = True
    result = None
    summary = None
    while(data):
        try: 
            result = requests.get('http://api.covid19api.com/summary')
            json = result.json()
            summary = json['Global']
            countries = json['Countries']
            data = False
        except:
            data = True
    return render(request, 'index.html',{'summary':summary,'countries':countries})

def country(request):
    data = True
    result = None
    while(data):
        try: 
            result = requests.get('http://api.covid19api.com/summary')
            json = result.json()
            countries = json['Countries']
            data = False
        except:
            data = True
    return render(request, 'country.html',{'countries':countries})