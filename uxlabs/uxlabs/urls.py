from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.contacts.urls', namespace='contacts')),
    url(r'^', include('apps.websites.urls', namespace='websites')),
    url(r'^', include('apps.info.urls', namespace='info')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
