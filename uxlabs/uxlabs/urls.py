from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.contacts.urls', namespace='contacts')),
    url(r'^', include('apps.websites.urls', namespace='websites')),
    url(r'^', include('apps.info.urls', namespace='info')),
]
