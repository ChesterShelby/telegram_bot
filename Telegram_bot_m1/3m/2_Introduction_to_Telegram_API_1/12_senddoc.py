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
            print(message)
            file_id = message['message']['document']['file_id']
            user_id = message['message']['from']['id']
            if user_id in ADMINS:
                requests.get(f'{BASE_URL}{TOKEN}/sendDocument?chat_id={user_id}&document={file_id}')


pulling()
