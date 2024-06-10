from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.index_view, name='artigos'),
    path('artigo/<int:artigo_id>/', views.artigo_view, name='artigo'),
    path('user/<int:user_id>/', views.user_view, name='user'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('artigo/novo_post', views.novo_post_view, name="novo_post"),
]