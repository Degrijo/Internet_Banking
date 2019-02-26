from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm


class User(AbstractUser):
    money = models.IntegerField(default=0)

    def update_money(self, money):
        self.money += money
        self.save()
