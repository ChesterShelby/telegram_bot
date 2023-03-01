import requests

BASE_URL = 'https://api.telegram.org/bot'

TOKEN = '6128647054:AAGdU2hOxoOC-7Sx5wzad3ySeDVbQtUy9Gk'


def get_updates():
   r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
   print(r.json()['result'][-1]['message']['from'])


get_updates()

"""
Chat - этот объект представляет собой чат.

id - Уникальный id чата

type - Тип чата: “private”, “group”, “supergroup” или “channel”

title - Название, для каналов или групп(Необязательный параметр)

username -  Username, для чатов и некоторых каналов(Необязательный параметр)

first_name - Имя собеседника в чате(Необязательный параметр)

last_name -  Фамилия собеседника в чате(Необязательный параметр)

all_members_are_administrators - True, если все участники чата являются администраторами(Необязательный параметр)

"""