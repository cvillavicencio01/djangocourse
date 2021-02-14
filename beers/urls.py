from django.urls import path, re_path
from . import views

app_name = 'beers'

urlpatterns = [
    path('', views.brewery, name='brewery'),
    re_path(r'(?P<brewery_id>[0-9]+)/$', views.brewery_details, name='brewery_details'),
]