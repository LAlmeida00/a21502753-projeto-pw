from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'projetoPortfolioPW'

urlpatterns = [
    path('', views.index_view, name='projetoPortfolioPW'),
    path('curso/<int:curso_id>/', views.curso_view, name='curso'),
    path('disciplinas/', views.disciplinas_view, name='disciplinas'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina'),
    path('projeto/<int:disciplina_id>/', views.projeto_view, name='projeto'),

    # edicao dos dados
    path('curso/novo', views.novo_curso_view, name="novo_curso"),
    path('curso/<int:curso_id>/editar', views.editar_curso_view,name="editar_curso"),
    path('curso/<int:curso_id>/apagar', views.apagar_curso_view, name="apagar_curso"),
    path('disciplina/nova/', views.nova_disciplina_view, name='nova_disciplina'),
    path('disciplina/<int:disciplina_id>/editar/', views.editar_disciplina_view, name='editar_disciplina'),
    path('disciplina/<int:disciplina_id>/apagar/', views.apagar_disciplina_view, name='apagar_disciplina'),
    path('disciplina/<int:disciplina_id>/novo_projeto/', views.novo_projeto_view, name='novo_projeto'),



    # registo login e logout
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    # recuperação de password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='projetoPortfolioPW/registration/password_reset_form.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='projetoPortfolioPW/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='projetoPortfolioPW/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='projetoPortfolioPW/registration/password_reset_complete.html'), name='password_reset_complete'),
]