"""
Напишем прототип бота, который получает сообщения, проверяет новое ли оно и если новое,
а также если это написал пользователь-администратор и текст равен /start,
он будет отсылать нам обратно сообщение с Привет username
"""

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
            user_id = message['message']['from']['id']
            user_name = message['message']['from']['username']
            text = message['message']['text']
            if user_id in ADMINS and text == '/start':
                requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text=Привет {user_name}')


pulling()
