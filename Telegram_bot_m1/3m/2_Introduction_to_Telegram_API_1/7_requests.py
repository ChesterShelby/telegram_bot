import requests

BASE_URL = 'https://api.telegram.org/bot'

TOKEN = '6128647054:AAGdU2hOxoOC-7Sx5wzad3ySeDVbQtUy9Gk'


def get_updates():
    r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
    print(r.json()['result'][-1]['message'])


get_updates()
