from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'clanwebsite'

urlpatterns = [
    path('', views.index_view, name='home'), # Rota da página inicial
    path('index/', views.index_view, name='home'), # Rota da página inicial
    path('gallery/', views.gallery_view, name='gallery'),  # Página da galeria
    path('about/', views.about_view, name='about'),  # Página sobre o clan
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)