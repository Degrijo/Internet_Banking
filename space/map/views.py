from django.shortcuts import render
import requests


def view_map(request):
    return render(request, 'map/map.html', get_atms())


def get_atms():
    r = requests.post("https://belarusbank.by/api/atm").json()
    atms = {"Минск": [], "Гродно": [], "Гомель": [], "Витебск": [], "Брест": [], "Могилев": []}
    for dic in r:
        if dic["city"] in atms.keys() and len(atms[dic["city"]])<10:
            atms[dic["city"]].append(dic["address_type"]+" "+dic["address"]+" "+dic["house"])
    return atms
