from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_home, name='view_home'),
    url(r'^link/', views.view_home, name='view_home'),
    url(r'^mytransactions/', views.view_home, name='view_home'),
]
