from django.shortcuts import render
import requests


def view_home(request):
    return render(request, 'appmain/home.html')


def course_of_money(request):
    r = requests.post("https://belarusbank.by/api/kursExchange", data={"city": "Minsk"})
    return render(request, 'templates/appmain/money.html')
 # {"values": r.text}
