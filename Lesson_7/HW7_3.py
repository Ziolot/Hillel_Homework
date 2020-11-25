import requests
import datetime

URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'


def format_value(val):
    if val >= 0:
        result = ' {:.2f}'.format(val)
    else:
        result = '{:.2f}'.format(val)
    return result


def return_weather():
    city_name = input('Enter your city: ')
    cnt = input('Enter number of day: ')
    data = {'q': city_name, 'units': 'metric', 'cnt': cnt,
            'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()


def weather_file():
    result = return_weather()
    with open('dw.txt', 'w') as f:
        f.writelines(['Date\t\t Day temperature\t Feelings during the day\t Night temperature', '\n'])
        for day in result['list']:
            f.writelines([datetime.date.fromtimestamp(day['dt']).strftime('%d-%m-%Y') + (12 * ' '),
                          format_value(day['temp']['day']) + (16 * ' '),
                          format_value(day['feels_like']['day']) + (24 * ' '),
                          format_value(day['temp']['night']), '\n'])


weather_file()
