from django.shortcuts import render
import requests


def view_home(request):
    return render(request, 'appmain/wrapper.html')


def course_of_money(request):
    # r = requests.post("https://belarusbank.by/api/kursExchange", data={"city": "Minsk"})
    return render(request, 'appmain/money.html')
 # {"values": r.text}
