from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetConfirmView
from django.http import HttpResponse
from .models import Banda, Album, Musica
from .forms import BandaForm, AlbumForm, MusicaForm


GRUPOS_PERMITIDOS = ['editores_de_bandas', 'admin_de_bandas']

# Create your views here.

def index_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome')
    }
    return render(request, "bandas/index.html", context)


def banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    context = {
        'banda':banda,
        'albums': banda.albuns.all().order_by('ano')
    }
    return render(request, 'bandas/banda.html', context)


def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {
        'album': album,
        'musicas': album.musicas.all().order_by('nome')
    }
    return render(request, 'bandas/album.html', context)


def musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    album = musica.album
    context = {
        'album': album,
        'musica': musica,
    }
    return render(request, 'bandas/musica.html', context)

# ------------------------------------------------------------------------------

#Registo
def registo_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Verificar se o username já está em uso
        if User.objects.filter(username=username).exists():
            return render(request, 'bandas/registo.html', {'mensagem': 'O username já está em uso'})

        # Criar username estiver disponível
        user = models.User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        grupo = Group.objects.get(name='editores_de_bandas')
        user.groups.add(grupo)

        return redirect('login')

    return render(request, 'bandas/registo.html')


#Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.groups.filter(name__in=GRUPOS_PERMITIDOS).exists():
            login(request, user)  # Ligacao login do utilizador

            # Guardar a informaçao do utilizador na sessão
            request.session['user_id'] = user.id
            request.session['user_groups'] = list(user.groups.values_list('name', flat=True))
            return redirect('/bandas')
        else:
            return render(request, 'bandas/login.html', {'mensagem': 'Credenciais inválidas'})

    return render(request, 'bandas/login.html')


#Logout
def logout_view(request):
    logout(request)
    return redirect('/bandas')

# ------------------------------------------------------------------------------

#bandas
@login_required
def nova_banda_view(request):
    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.add_banda'):
        form = BandaForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas')

        context = {'form': form}
        return render(request, 'bandas/nova_banda.html', context)
    else:
        return HttpResponse("403: ACESSO NEGADO")


@login_required
def editar_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.change_banda'):
        if request.POST:
            form = BandaForm(request.POST, instance=banda)
            if form.is_valid():
                form.save()
                return redirect('bandas:bandas')
        else:
            form = BandaForm(instance=banda)

        context = {'form': form, 'banda': banda}
        return render(request, 'bandas/editar_banda.html', context)
    else:
        return HttpResponse("403: ACESSO NEGADO")


@login_required
def apagar_banda_view(request, banda_id):
    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.delete_banda'):
        banda = Banda.objects.get(id=banda_id)
        banda.delete()
        return redirect('bandas:bandas')
    else:
        return HttpResponse("403: ACESSO NEGADO")

# ------------------------------------------------------------------------------

#albums
@login_required
def novo_album_view(request):
    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.add_album'):
        form = AlbumForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas')

        context = {'form': form}
        return render(request, 'bandas/novo_album.html', context)
    else:
        return HttpResponse("403: ACESSO NEGADO")


@login_required
def editar_album_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.change_album'):
        if request.POST:
            form = AlbumForm(request.POST, instance=album)
            if form.is_valid():
                form.save()
                return redirect('bandas:album', album_id=album.id)
        else:
            form = AlbumForm(instance=album)

        context = {'form': form, 'album': album}
        return render(request, 'bandas/editar_album.html', context)
    else:
        return HttpResponse("403: ACESSO NEGADO")


@login_required
def apagar_album_view(request, album_id):
    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.delete_album'):
        album = Album.objects.get(id=album_id)
        album.delete()
        return redirect('bandas:bandas')
    else:
        return HttpResponse("403: ACESSO NEGADO")

# ------------------------------------------------------------------------------

#musicas
@login_required
def nova_musica_view(request):
    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.add_musica'):
        form = MusicaForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas')

        context = {'form': form}
        return render(request, 'bandas/nova_musica.html', context)
    else:
        return HttpResponse("403: ACESSO NEGADO")


@login_required
def editar_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.change_musica'):
        if request.POST:
            form = MusicaForm(request.POST, instance=musica)
            if form.is_valid():
                form.save()
                return redirect('bandas:musica', musica_id=musica.id)
        else:
            form = MusicaForm(instance=musica)

        context = {'form': form, 'musica': musica}
        return render(request, 'bandas/editar_musica.html', context)
    else:
        return HttpResponse("403: ACESSO NEGADO")


@login_required
def apagar_musica_view(request, musica_id):
    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('bandas.delete_musica'):
        musica = Musica.objects.get(id=musica_id)
        musica.delete()
        return redirect('bandas:bandas')
    else:
        return HttpResponse("403: ACESSO NEGADO")

# ------------------------------------------------------------------------------
