import requests

BASE_URL = 'https://api.telegram.org/bot'

TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
ADMINS = [5968438033]


def pulling():
    count_message = 0
    while True:
        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        if count_message != len(response['result']):
            count_message = len(response['result'])
            message = response['result'][-1]
            user_id = message['message']['from']['id']
            if user_id in ADMINS:
                requests.get(
                    f'{BASE_URL}{TOKEN}/sendVenue?chat_id={user_id}&latitude=55.53932&longitude=37.39892&title=Moscow')


pulling()
