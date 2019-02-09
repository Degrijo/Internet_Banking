from django.shortcuts import render
from .models import User


def view_transact(request):
    return render(request, 'mytransactions/transactions.html')


def upd_mon(request):
    getter = User.objects.get(id=request.POST['id'])
    getter.update_money(int(request.POST['money']))
    return render(request, "mytransactions/submit_form.html")
