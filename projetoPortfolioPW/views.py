from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Curso, Disciplina, Projeto, AreaCientifica
from .forms import CursoForm, DisciplinaForm, ProjetoForm

# Create your views here.

def index_view(request):
    areas_cientificas = AreaCientifica.objects.all()
    cursos = Curso.objects.all()
    context = {
        'areas_cientificas': areas_cientificas, 'cursos': cursos
    }
    return render(request, 'projetoPortfolioPW/index.html', context)

def curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    disciplinas = Disciplina.objects.filter(curso_id=curso_id)
    context = {
        'curso': curso, 'disciplinas': disciplinas
    }
    return render(request, 'projetoPortfolioPW/curso.html', context)

def disciplinas_view(request):
    disciplinas = Disciplina.objects.all()
    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'projetoPortfolioPW/disciplinas.html', context)

def disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    context = {
        'disciplina': disciplina
    }
    return render(request, 'projetoPortfolioPW/disciplina.html', context)

def projeto_view(request, disciplina_id):
    projeto = Projeto.objects.get(disciplina_id=disciplina_id)
    context = {
        'projeto': projeto
    }
    return render(request, 'projetoPortfolioPW/projeto.html', context)

# ------------------------------------------------------------------------------

#registo e login e logout

def registo_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['nome']
        last_name=request.POST['apelido']
        password = request.POST['password']

        # Verificar se o username já está em uso
        if User.objects.filter(username=username).exists():
            return render(request, 'projetoPortfolioPW/registo.html', {'mensagem': 'O username já está em uso'})

        # Criar username estiver disponível
        user = models.User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        return redirect('projetoPortfolioPW:login')

    return render(request, 'projetoPortfolioPW/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('projetoPortfolioPW:projetoPortfolioPW')
        else:
            return render(request, 'projetoPortfolioPW/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'projetoPortfolioPW/login.html')

def logout_view(request):
    logout(request)
    return redirect('projetoPortfolioPW:projetoPortfolioPW')

# ------------------------------------------------------------------------------

#curso

@login_required
def novo_curso_view(request):

    form = CursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projetoPortfolioPW:projetoPortfolioPW')

    context = {'form': form}
    return render(request, 'projetoPortfolioPW/novo_curso.html', context)

@login_required
def editar_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)

    if request.POST:
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('projetoPortfolioPW:curso', curso_id=curso_id)
    else:
        form = CursoForm(instance=curso)

    context = {'form': form, 'curso': curso}
    return render(request, 'projetoPortfolioPW/editar_curso.html', context)

@login_required
def apagar_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('projetoPortfolioPW:projetoPortfolioPW')

# ------------------------------------------------------------------------------

#Disciplina

@login_required
def nova_disciplina_view(request):

    form = DisciplinaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projetoPortfolioPW:disciplinas')

    context = {'form': form}
    return render(request, 'projetoPortfolioPW/nova_disciplina.html', context)

@login_required
def editar_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)

    if request.POST:
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('projetoPortfolioPW:disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)

    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'projetoPortfolioPW/editar_disciplina.html', context)

@login_required
def apagar_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('projetoPortfolioPW:disciplinas')

# ------------------------------------------------------------------------------

#Projeto

@login_required
def novo_projeto_view(request):

    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projetoPortfolioPW:disciplinas')

    context = {'form': form}
    return render(request, 'projetoPortfolioPW/novo_projeto.html', context)

@login_required
def editar_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetoPortfolioPW:projeto', disciplina_id=projeto.disciplina_id)
    else:
        form = ProjetoForm(instance=projeto)

    context = {'form': form, 'projeto': projeto}
    return render(request, 'projetoPortfolioPW/editar_projeto.html', context)

@login_required
def apagar_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('projetoPortfolioPW:disciplina', disciplina_id=projeto.disciplina_id)

# ------------------------------------------------------------------------------


