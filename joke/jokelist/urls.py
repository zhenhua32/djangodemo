from django.conf.urls import url
from . import views

# Namespacing URL names
app_name = 'jokelist'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
