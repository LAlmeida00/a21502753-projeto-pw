from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('meteo_prox_5_days/', views.meteo_prox_days_view, name='meteo_prox_5_days'),

    #API endpoints
    path('api/', views.api_meteo_view, name='api_meteo'),
    path('api/cities/', views.api_city_list_view, name='api_city_list'),
    path('api/weather/today/<str:city_name>/', views.api_today_weather_view, name='api_today_weather'),
    path('api/weather/5days/<str:city_name>/', views.api_5_days_weather_view, name='api_5_days_weather'),
]
