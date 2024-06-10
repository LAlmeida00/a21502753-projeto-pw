from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.index_view, name='filmes'),
    path('filme/<int:filme_id>/', views.detalhes_filme_view, name='detalhes_filme'),
]