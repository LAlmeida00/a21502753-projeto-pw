from django.shortcuts import render
from .models import Filme, Ator, Genero

# Create your views here.

def index_view(request):
    generos = Genero.objects.all()
    filmes_por_genero = {}

    for genero in generos:
        filmes_por_genero[genero] = Filme.objects.filter(generos=genero)

    context = {
        'filmes_por_genero': filmes_por_genero
    }
    return render(request, "filmes/index.html", context)

def detalhes_filme_view(request, filme_id):
    filme = Filme.objects.get(pk=filme_id)
    context = {
        'filme': filme
    }
    return render(request, "filmes/detalhes_filme.html", context)