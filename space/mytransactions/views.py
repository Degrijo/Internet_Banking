from django.shortcuts import render
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


@login_required(login_url='not_logged/')
def crediting_yourself(request):
    return render(request, 'mytransactions/crediting_yourself.html')


@login_required(login_url='not_logged/')
def money_transfer(request):
    return render(request, 'mytransactions/money_transfer.html')


@login_required(login_url='not_logged/')
def show_money(request):
    return render(request, 'mytransactions/show_cash.html')


def not_logged(request):
    return render(request, 'mytransactions/not_logged_in.html')


def submit_transfer(request):
    user = request.user
    try:
        getter = User.objects.get(id=request.POST['id'])
        if getter.id != user.id:
            if user.money >= int(request.POST['money']):
                user.update_money((-1) * int(request.POST['money']))
                getter.update_money(int(request.POST['money']))
                rezult = "Operation done"
            else:
                rezult = "You don't have enough money"
        else:
            rezult = "Recipient and sender is one person. Use 'Crediting yourself'"
    except ObjectDoesNotExist:
        rezult = "User with such id doesn't exist"
    return render(request, "mytransactions/submit_transfer.html", {"rezult": rezult})


def submit_cred(request):
    user = request.user
    user.update_money(int(request.POST['money']))
    rezult = "Operation done"
    return render(request, "mytransactions/submit_cred.html", {"rezult": rezult})
