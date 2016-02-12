from django.conf.urls import include, url, patterns
from django.contrib import admin

from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    #        url(r'^',include ('perfis.urls')),

]
