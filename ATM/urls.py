from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('appmain.urls')),
    url(r'^show_money/', include('mytransactions.urls')),
    url(r'^rate/', include('rate.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^map/', include('map.urls')),
    url(r'^reg/', include('registration.urls'))
]
