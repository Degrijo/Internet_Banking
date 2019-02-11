from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_money, name='show_money'),
    url('^crediting_yourself/$', views.crediting_yourself),
    url('^crediting_yourself/submit_cred$', views.submit_cred),
    url('^money_transfer/submit_transfer$', views.submit_transfer),
    url('^money_transfer/$', views.money_transfer)
]
