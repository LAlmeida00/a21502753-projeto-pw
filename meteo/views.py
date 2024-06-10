import requests
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse

owner = "a21502753"
local_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
weather_type_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'


def index_view(request):

    city_name = "Lisboa"
    weather_day = "0"
    context = weather_view(city_name, weather_day)

    return render(request, 'meteo/index.html', context)


def weather_view(city_name, weather_day):

    response = requests.get(local_url)
    data = response.json()

    # Iterando sobre os dados para encontrar a cidade desejada
    city_id = None
    for item in data['data']:
        if item['local'] == city_name:
            city_id = item['globalIdLocal']
            break

    weather_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()['data'][int(weather_day)]


    weather_type_response = requests.get(weather_type_url)
    weather_types = {entry['idWeatherType']: entry['descWeatherTypePT'] for entry in weather_type_response.json()['data']}

    # Determina qual e o tipo de ícone a ser usado (dia ou noite)
    idWeatherType = weather_data["idWeatherType"]
    id_num = str(idWeatherType).zfill(2) if idWeatherType < 10 else str(idWeatherType)
    current_hour = datetime.now().hour
    is_daytime = 6 <= current_hour < 18
    icon_type = 'd' if is_daytime else 'n'
    icon_url = f'/static/meteo/icones/w_ic_{icon_type}_{id_num}anim.svg'

    context = {
        'city': city_name,
        'temp_min': weather_data['tMin'],
        'temp_max': weather_data['tMax'],
        'data': weather_data['forecastDate'],
        'weather': weather_types[weather_data['idWeatherType']],
        'icon_url': icon_url,
    }

    return context


def meteo_prox_days_view(request):
    locations = get_local_data_api()

    # Verifica se o formulário foi submetido e se há uma seleção na caixa de seleção
    if request.method == 'POST' and 'location' in request.POST:
        selected_location = request.POST.get('location')

        # Verifica se a seleção não é de Lisboa
        if selected_location != 'Lisboa':
            city_name = selected_location
        else:
            city_name = 'Lisboa'
    else:
        # Se o formulário não foi submetido ou se não houver seleção, mantém Lisboa como padrão
        city_name = 'Lisboa'


    weather_days = []
    for weather_day in range(5):
        context = weather_view(city_name, str(weather_day))
        weather_days.append(context)

    context = {
        'locations': locations,
        'weather_days': weather_days,
        'selected_location': city_name,
    }
    return render(request, 'meteo/meteo_prox_5_days.html', context)


def get_local_data_api():
    response = requests.get(local_url)
    if response.status_code == 200:
        dic_data = response.json()
        locations = [item['local'] for item in dic_data['data']]
        return locations
    else:
        return []

def api_meteo_view(request):
    return render(request, 'meteo/api_meteo.html')


def api_city_list_view(request):
    data = get_local_data_api()

    context = {
        "owner": owner,
        "data": data,
    }

    return JsonResponse(context)


def api_today_weather_view(request, city_name):
    data = weather_view(city_name, "0")

    context = {
        "owner": owner,
        "data": data,
    }

    return JsonResponse(context)


def api_5_days_weather_view(request, city_name):
    weather_days = []
    for weather_day in range(5):
        data = weather_view(city_name, str(weather_day))
        weather_days.append(data)

    context = {
        "owner": owner,
        "data": weather_days,
    }

    return JsonResponse(context)
