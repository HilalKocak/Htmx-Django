from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    context=dict()
    return render(request, 'homepage.html', context)


def create_dashboard(request):
    context=dict()
    return render(request, 'dashboard.html', context)
