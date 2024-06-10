from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout, get_user_model
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required
from .models import User, Post, PostImage, Comment, Rating
from .forms import UserForm, PostForm, CommentForm

# Create your views here.

def index_view(request):
    artigos = Post.objects.all()
    context = {
        'artigos': artigos
    }
    return render(request, "artigos/index.html", context)

def artigo_view(request, artigo_id):
    artigo = Post.objects.get(id=artigo_id)
    imagens = PostImage.objects.filter(post=artigo)
    comentarios = Comment.objects.filter(post=artigo)

    context = {
        'artigo': artigo,
        'imagens': imagens,
        'comentarios': comentarios,
    }
    return render(request, "artigos/artigo.html", context)

def user_view(request, user_id):
    user = User.objects.get(id=user_id)
    artigos = Post.objects.filter(user=user)
    comentarios = Comment.objects.filter(user=user)
    total_artigos = artigos.count()
    total_comentarios = comentarios.count()
    context = {
        'user': user,
        'artigos': artigos,
        'comentarios': comentarios,
        'total_artigos': total_artigos,
        'total_comentarios': total_comentarios,
    }
    return render(request, "artigos/user.html", context)

# ------------------------------------------------------------------------------

#registo e login e logout

def registo_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['nome']
        last_name = request.POST['apelido']
        password = request.POST['password']

        # Verificar se o username já está em uso
        if AuthUser.objects.filter(username=username).exists():
            return render(request, 'artigos/registo.html', {'mensagem': 'O username já está em uso'})

        # Criar um novo objeto User no seu modelo personalizado
        user = User.objects.create(
            user=username,
            image_profile=None  # Ajuste conforme necessário
        )

        # Criar username com create_user
        auth_user = AuthUser.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        return redirect('artigos:login')

    return render(request, 'artigos/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('artigos:artigos')
        else:
            return render(request, 'artigos/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'artigos/login.html')

def logout_view(request):
    logout(request)
    return redirect('artigos:artigos')

# ------------------------------------------------------------------------------

def novo_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user_model = get_user_model()
            user = user_model.objects.get(pk=request.user.pk)
            form.save(user=user)
            return redirect('artigos:artigos')
    else:
        form = PostForm()
    return render(request, 'artigos/novo_post.html', {'form': form})






