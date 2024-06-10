from django.shortcuts import render
from datetime import datetime  # Importe o módulo datetime

# Create your views here.

def index_view(request):
    current_date = datetime.now() # Obtém a data atual
    return render(request, "clanwebsite/index.html", {'current_date': current_date})

def gallery_view(request):
    current_date = datetime.now() # Obtém a data atual
    return render(request, "clanwebsite/gallery.html", {'current_date': current_date})

def about_view(request):
    current_date = datetime.now() # Obtém a data atual
    return render(request, "clanwebsite/about.html", {'current_date': current_date})