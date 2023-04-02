from django.contrib import admin
from django.urls import include, path
from charts.views import home

urlpatterns = [

    path("", home, name='home'),
]
