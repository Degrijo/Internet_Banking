from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_of_money, name='course_of_money'),
]