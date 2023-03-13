"""
unbanChatMember - Используйте этот метод, чтобы отменить блокировку ранее удаленного пользователя в супергруппе.
Пользователь не вернется в группу автоматически, но сможет присоединиться по ссылке и т.д. Чтобы это сработало,
бот должен быть администратором в группе. Возвращает значение True при успешном выполнении.

chat_id - Уникальный идентификатор целевой группы или имя пользователя целевой супергруппы (в формате @supergroupusername)
user_id - Уникальный идентификатор целевого пользователя
"""

import requests

BASE_URL = 'https://api.telegram.org/bot'

TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
ADMINS = [5968438033]

kik_id = 308713460  # @ChesterShelby


def pulling():
    count_message = 0
    while True:
        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        if count_message != len(response['result']):
            count_message = len(response['result'])
            message = response['result'][-1]
            print(message)
            chat_id = message['message']['chat']['id']
            user_id = message['message']['from']['id']
            print(user_id)
            if user_id == kik_id:
                requests.get(f"{BASE_URL}{TOKEN}/",
                             json={'method': 'unbanChatMember', 'chat_id': chat_id, 'user_id': user_id})


pulling()
