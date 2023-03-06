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
            requests.get(f"{BASE_URL}{TOKEN}/",
                         json={'method': 'sendMessage', 'chat_id': f'{user_id}', 'text': 'Inline клавиатура',
                               'reply_markup': {'keyboard': [[{'text': 'Google', 'url': 'www.google.com'},
                                                              {'text': 'Callback', 'callback_data': 'button'}],
                                                             ]},
                               })


pulling()
