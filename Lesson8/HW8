import requests
import json
import datetime

URL = 'https://api.exchangerate.host/convert'

def symbols():
    with open('symbols.json', 'r') as file:
        symbols_file = json.load(file)
    return symbols_file

def currency_input():
    currency_from = input("Type the 3 letter abbreviation of the currency FROM convert. By default it will take USD ")
    if currency_from == "":
        currency_from = 'USD'
    currency_to = input('Type in the 3 letter abbreviation of the currency TO convert. By default UAH ')
    if currency_to == '':
        currency_to = 'UAH'
    currency_amount = input('Type in amount to convert. By default 100 ')
    if currency_amount == '':
        currency_amount = 100.00
    currency_date = input('Type in date in a format "YYYY-MM-dd". By default today ')
    if currency_date == '':
        currency_date = datetime.datetime.now()
    data = {'from': currency_from, 'to': currency_to, 'amount': currency_amount, 'date': currency_date}
    print(data)
    r = requests.get(URL, data)
    print(r.json())


currency_input()
