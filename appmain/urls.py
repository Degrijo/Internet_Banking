from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_home, name='index'),
    url(r'^link/', views.view_home, name='index'),
    url(r'^mytransactions/', views.view_home, name='index'),
    url(r'^money/', views.course_of_money, name='index'),
]
