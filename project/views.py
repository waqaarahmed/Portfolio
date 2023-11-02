from django.shortcuts import render
from django.http import HttpResponse
from .models import project

# Create your views here.
def index(request):
   return render(request, 'portfolio/index.html')
   

def home(request):
    Project = project.objects.all()
    return render(request, 'home.html', {'Project':Project})
