from django.shortcuts import render
from .models import Spot

# Create your views here.

def home(request):
    return render (request, 'home.html')


def list_cocheras(request):
    # Traemos todos los spots ordenados por número
    cocheras = Spot.objects.all().order_by('numero')
    return render(request, 'gestion/main.html', {'cocheras': cocheras})