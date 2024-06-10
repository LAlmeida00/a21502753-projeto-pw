from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def gallery_view(request):
    return HttpResponse("Explore a nossa galeria de imagens e vídeos nesta página!")

def about_view(request):
    return HttpResponse("Bem-vindo à página 'Sobre', onde podes saber mais sobre nós!")

def contact_view(request):
    return HttpResponse("Esta é a página de contato. Entre em contato conosco para mais informações.")