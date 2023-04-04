from django.contrib import admin
from django.urls import include, path
from charts.views import home, dashboard, upload_view

app_name='charts'
urlpatterns = [

    path("<pk>/", dashboard, name='dashboard'),
    path("upload/<pk>", upload_view, name='upload_view'),
]
