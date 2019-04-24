from django.shortcuts import render
from mytransactions.models import User
from django.contrib.auth import authenticate, login, logout


def show_reg_page(request):
    return render(request, 'registration/reg_page.html')


def new_user(request):
    user = User.objects.create_user(request.POST['username'], password=request.POST['password'], email=request.POST['mail'])
    user.save()
    authenticate(user)
    login(request, user)
    return render(request, 'appmain/wrapper.html')


def show_log_in_page(request):
    return render(request, 'registration/log_in_page.html')


def authorize(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return render(request, 'appmain/wrapper.html')
    else:
        return render(request, 'registration/wrong_password.html')


def show_log_out_page(request):
    logout(request)
    return render(request, 'appmain/wrapper.html')
