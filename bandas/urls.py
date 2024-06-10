from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name='bandas'),
    path('banda/<int:banda_id>/', views.banda_view, name='banda'),
    path('album/<int:album_id>/', views.album_view, name='album'),
    path('musica/<int:musica_id>/', views.musica_view, name='musica'),


    # edicao dos dados
    path('banda/novo', views.nova_banda_view, name="nova_banda"),
    path('banda/<int:banda_id>/editar', views.editar_banda_view, name="editar_banda"),
    path('banda/<int:banda_id>/apaga/', views.apagar_banda_view, name="apagar_banda"),
    path('album/novo/', views.novo_album_view, name="novo_album"),
    path('album/<int:album_id>/editar', views.editar_album_view, name="editar_album"),
    path('album/<int:album_id>/apaga/', views.apagar_album_view, name="apagar_album"),
    path('musica/novo/', views.nova_musica_view, name="nova_musica"),
    path('musica/<int:musica_id>/editar', views.editar_musica_view, name="editar_musica"),
    path('musica/<int:musica_id>/apaga/', views.apagar_musica_view, name="apagar_musica"),

    # registo login e logout
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    # recuperação de password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='bandas/registration/password_reset_form.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='bandas/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='bandas/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='bandas/registration/password_reset_complete.html'), name='password_reset_complete'),
]

