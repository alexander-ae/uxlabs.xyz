from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^websites/$', views.websites, name='websites'),
    url(r'^websites/(?P<slug>[-\w]+)/$', views.detalle, name='detalle'),
]
