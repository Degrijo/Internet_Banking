from django.shortcuts import render
import requests


def course_of_money(request):
    return render(request, 'rate/rate.html')
# r = requests.post("https://belarusbank.by/api/kursExchange", data={"city": "Minsk"})
# {"values": r.text}
