from django.urls import path
from . import views

app_name = 'pwsite'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('index/', views.index_view, name='index'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('sobre/', views.sobre_view, name='sobre'),
]