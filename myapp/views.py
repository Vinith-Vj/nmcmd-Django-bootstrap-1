from django.shortcuts import render
from .models import Service

# Create your views here.

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})