from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_reg_page, name='show_reg_page'),
    url(r'^log_in', views.show_log_in_page, name='show_log_in_page'),
    url(r'^accept_reg', views.new_user, name='new_user'),
    url(r'^accept_login', views.authorize, name='authorize'),
    url(r'^log_out', views.show_log_out_page, name='show_log_out_page'),
]
