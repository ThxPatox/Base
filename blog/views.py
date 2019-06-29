from django.shortcuts import render
from .models import Estacionamiento

def index(request):
    posts = Estacionamiento.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})