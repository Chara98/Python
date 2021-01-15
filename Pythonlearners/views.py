from django.shortcuts import render
from .models import members
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def join(request):
    return render(request,'join.html')

def  peo(request):
    mems = members.objects.all()
    return render(request, 'peo.html', {'mems':mems})
