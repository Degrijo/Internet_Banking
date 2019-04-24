from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_reg_page, name='show_reg_page'),
    path('log_in/', views.show_log_in_page, name='show_log_in_page'),
    path('accept_reg/', views.new_user, name='new_user'),
    path('accept_login/', views.authorize, name='authorize'),
    path('log_out/', views.show_log_out_page, name='show_log_out_page'),
]
