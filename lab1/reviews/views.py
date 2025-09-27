from django.shortcuts import render

# Create your views here.

from .models import Review

def index(request):
    params = {}
    return render(request, "index.html", params)