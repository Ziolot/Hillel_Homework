import requests

URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'


def myweather(city, days):
    data = {'q': city, 'units': 'metric', 'cnt': days,
            'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()


def write_to_file(result):
    with open('OdWeather.txt', 'w+') as f:
     f.writelines(['Day', 'Night', 'Something', '\n'])
    for day in result['list']:
        f.writelines([str(day['temp']['day']) + '    ',
                      str(day['temp']['night']) + '    ',
                      'something ', '\n'])


def user_input():
    city = input('Enter city: ')
    count = input('Enter count: ')
    result = myweather(city, count)
    write_to_file(result)

  user_input()
