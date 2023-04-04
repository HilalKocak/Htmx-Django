from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Dashboard, DataFile
from .forms import DataForm

# Create your views here.


def home(request):
    context=dict()
    return render(request, 'homepage.html', context)


def create_dashboard(request):
    length = request.user.dashboard_set.filter(title__icontains='Untitled').count()
    index = '' if length==0 else str(length)

    instance = Dashboard.objects.create(
        user = request.user,
        title = 'Untitled{}'.format(index),
    )
    instance.save()
    
    return redirect('charts:dashboard', instance.id) # we have name:dashboard in url
# I specified app_name:charts in the views. thats why if I didnt write charts:dashboard, it will not recognize

def dashboard(request, pk):
    dashboard = Dashboard.objects.get(id=pk)
    context=dict(
        dashboard = dashboard,
        pk = pk,
    )
    return render(request, 'charts/dashboard.html', context)

def upload_view(request, pk):
    form= DataForm()
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            datafile = form.save(commit=False)
            datafile.user = request.user
            datafile.dashboard = request.user.dashboard_set.get(id=pk)
            datafile.workingfile = request.FILES['workingfile']
            datafile.save()
           
            redirect('charts:dashboard', pk)
    context=dict(
        form = form,
        pk=pk,
    )
    return render(request, 'charts/upload_data.html',context )
