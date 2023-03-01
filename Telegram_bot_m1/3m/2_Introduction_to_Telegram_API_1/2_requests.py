import requests

BASE_URL = 'https://api.telegram.org/bot'

TOKEN = '6128647054:AAGdU2hOxoOC-7Sx5wzad3ySeDVbQtUy9Gk'


def get_updates():
    r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
    message = r.json()['result'][-1]['message']['text']
    print(message)


get_updates()
"""
Этот метод не будет работать, если у вас уже подключен webhook.
"""


def get_updates():
    r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates?offset=1&timeout=10')
    print(r.json()['result'][-1])


get_updates()

"""
Во избежания повторяющихся обновлений, рекомендуется высчитывать offset каждый раз заново.
"""
