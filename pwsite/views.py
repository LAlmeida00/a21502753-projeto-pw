from django.shortcuts import render
from datetime import datetime

def index_view(request):
    current_date = datetime.now()
    return render(request, "pwsite/index.html", {'current_date': current_date})

def sobre_view(request):
    current_date = datetime.now()
    return render(request, "pwsite/sobre.html", {'current_date': current_date})

def interesses_view(request):
    current_date = datetime.now()
    return render(request, "pwsite/interesses.html", {'current_date': current_date})