from django.contrib import admin
from django.urls import path, include
import appmain.views
import map.views
import rate.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appmain.views.view_home, name='view_home'),
    path('show_money/', include('mytransactions.urls')),
    path('rate/', rate.views.course_of_money, name='course_of_money'),
    path('news/', include('news.urls')),
    path('map/', map.views.view_map, name="view_map"),
    path('reg/', include('registration.urls'))
]
