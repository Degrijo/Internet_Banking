from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_transact, name='view_transact'),
    url('^upd_mon$', views.upd_mon)
]
