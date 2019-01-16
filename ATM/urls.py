from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('appmain.urls')),
    url(r'^mytransactions/', include('appmain.urls')),
    url(r'^link/', include('appmain.urls')),
    url(r'^money/', include('appmain.urls')),
    url(r'^news/', include('news.urls')),
]
