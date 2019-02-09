from django.shortcuts import render
import requests


def course_of_money(request):
    return render(request, 'rate/rate.html', getting_inf())


def getting_inf():
    r = requests.post("https://belarusbank.by/api/kursExchange").json()
    rate = {}
    for dic in r:
        if dic["name"] in ["Минск", "Гродно", "Гомель", "Витебск", "Брест", "Могилев"]:
            if dic["name"]+"_in" in rate.keys():
                if float(dic["USD_in"]) < rate[dic["name"]+"_in"]:
                    rate[dic["name"]+"_in"] = float(dic["USD_in"])
                if float(dic["USD_out"]) > rate[dic["name"]+"_out"]:
                    rate[dic["name"]+"_out"] = float(dic["USD_out"])
            else:
                rate.setdefault(dic["name"]+"_in", float(dic["USD_in"]))
                rate.setdefault(dic["name"]+"_out", float(dic["USD_out"]))
    return rate
