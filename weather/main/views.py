from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from googletrans import Translator

# Create your views here.
def index(request):
    city = 'Osh'
    country = 'Kyrgyzstan'
    cities = ['Osh', 'Bishkek', 'Batken', 'Naryn']
    number = [4, 45, -7, 11, -58, 47]
    return render(request, 'index.html', context={'my_city':city, 'my_country':country, 'my_cities':cities, 'numbers':number})

def weather(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        API_KEY = '6621546e1a94625a215c063e4320d66d'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data_dict = response.json()     # json - > dict
        translator = Translator()
        w_cond = translator.translate(data_dict['weather'][0]['description'], dest='ru').text
        Weather = f"Погода в городе {city_name.title()}: {w_cond}"
        # Temperature in city Osh: 295.51
        temp = f"Температура в городе {city_name.title()}: {data_dict['main']['temp'] }°C"
        # Condition of weather in city Osh: Rain
        cond = translator.translate(data_dict['weather'][0]['main'], dest='ru').text
        condition_weather = f"Прогноз погоды в городе {city_name.title()}: {cond}"
        # feels_like
        feels_like = f"Температура в городе {city_name.title()} ощущается как: {data_dict['main']['feels_like'] }°C"
        # temp_min
        min_temp = f"Минимальная температура в городе {city_name.title()}: {data_dict['main']['temp_min'] }°C"
        # temp_max
        max_temp = f"Максимальная температура в городе {city_name.title()}: {data_dict['main']['temp_max'] }°C"

        return render(request, 'index.html', context={'Weather':Weather, 'temp':temp, 'condition_weather':condition_weather, 'feels_like':feels_like, 'min_temp':min_temp, 'max_temp':max_temp})
        # print(city_name)