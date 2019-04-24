from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_money, name='show_money'),
    path('crediting_yourself/', views.crediting_yourself, name='crediting_yourself'),
    path('crediting_yourself/submit_cred/', views.submit_cred, name='submit_cred'),
    path('money_transfer/submit_transfer/', views.submit_transfer, name='submit_transfer'),
    path('money_transfer/', views.money_transfer, name='money_transfer'),
    path('not_logged/', views.not_logged, name='not_logged')
]
