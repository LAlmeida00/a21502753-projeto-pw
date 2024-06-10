from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import models, authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetConfirmView
from .models import Profile, Interest, Skill, Competency, Experience, SocialLink, Project
from django.http import HttpResponse
from .forms import ProfileForm, InterestFormSet, SkillFormSet, CompetencyFormSet, ExperienceFormSet, SocialLinkFormSet, ProjectForm


GRUPOS_PERMITIDOS = ['admin_de_portfolio']

def landing_page_view(request):
    # Obtenha o objeto Profile (supondo que você tenha apenas um perfil no banco de dados)
    profile = Profile.objects.first()



    # Passe todas essas informações como contexto para o template
    context = {
        'profile': profile,

    }

    # Renderize o template com o contexto
    return render(request, 'portfolio/index.html', context)


def resume_page_view(request):
    # Obter o objeto Profile (supondo que você tenha apenas um perfil no banco de dados)
    profile = Profile.objects.first()

    # Obtenha os interesses, habilidades, competências, experiências e links sociais relacionados a este perfil
    interests = Interest.objects.filter(profile=profile)
    skills = Skill.objects.filter(profile=profile)
    competencies = Competency.objects.filter(profile=profile)
    experiences = Experience.objects.filter(profile=profile)
    social_links = SocialLink.objects.filter(profile=profile)

    context = {
        'profile': profile,
        'interests': interests,
        'skills': skills,
        'competencies': competencies,
        'experiences': experiences,
        'social_links': social_links,
    }

    return render(request, 'portfolio/resume.html', context)

def portfolio_page_view(request):

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/portfolio.html', context)


# ------------------------------------------------------------------------------
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
            return redirect('portfolio:index')
        else:
            return render(request, 'portfolio/login.html', {'mensagem': 'Credenciais inválidas'})

    return render(request, 'portfolio/login.html')

#Logout
def logout_view(request):
    logout(request)
    return redirect('portfolio:index')


# ------------------------------------------------------------------------------
@login_required
def edit_profile_view(request):
    profile = Profile.objects.first()  # Obter o perfil que deseja editar
    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('portfolio.change_profile'):
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('portfolio:index')
        else:
            form = ProfileForm(instance=profile)
        context = {'form': form, 'profile': profile}
        return render(request, 'portfolio/edit_profile.html', context)
    else:
        return HttpResponse("403: ACESSO NEGADO")


@login_required
def edit_resume_view(request):
    profile = Profile.objects.first()  # Obter o perfil que deseja editar
    if any(group in request.session.get('user_groups', []) for group in GRUPOS_PERMITIDOS) and request.user.has_perm('portfolio.change_profile'):
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            interest_formset = InterestFormSet(request.POST, instance=profile)
            skill_formset = SkillFormSet(request.POST, instance=profile)
            competency_formset = CompetencyFormSet(request.POST, instance=profile)
            experience_formset = ExperienceFormSet(request.POST, instance=profile)
            social_link_formset = SocialLinkFormSet(request.POST, instance=profile)

            if (profile_form.is_valid() and interest_formset.is_valid() and skill_formset.is_valid() and
                    competency_formset.is_valid() and experience_formset.is_valid() and social_link_formset.is_valid()):
                profile_form.save()
                interest_formset.save()
                skill_formset.save()
                competency_formset.save()
                experience_formset.save()
                social_link_formset.save()
                return redirect('portfolio:index')
        else:
            profile_form = ProfileForm(instance=profile)
            interest_formset = InterestFormSet(instance=profile)
            skill_formset = SkillFormSet(instance=profile)
            competency_formset = CompetencyFormSet(instance=profile)
            experience_formset = ExperienceFormSet(instance=profile)
            social_link_formset = SocialLinkFormSet(instance=profile)

        context = {
            'profile_form': profile_form,
            'interest_formset': interest_formset,
            'skill_formset': skill_formset,
            'competency_formset': competency_formset,
            'experience_formset': experience_formset,
            'social_link_formset': social_link_formset,
        }
        return render(request, 'portfolio/edit_resume.html', context)
    else:
        return HttpResponse("403: ACESSO NEGADO")

@login_required
def edit_portfolio_view(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:portfolio')
    else:
        form = ProjectForm()

    context = {'form': form, 'projects': projects}
    return render(request, 'portfolio/edit_portfolio.html', context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio:edit_portfolio')
    return redirect('index')
