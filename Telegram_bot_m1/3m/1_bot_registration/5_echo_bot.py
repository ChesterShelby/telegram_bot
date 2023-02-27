"""
Прежде чем мы начнем изучать более детально разработку ботов давайте сравним
в написании простого эхо бота без использования сторонних модулей и с использованием aiogram.

Начнем с бота без модулей. Для начала создадим переменные в которые запишем адрес,
по которому мы будем отправлять запросы, а также переменную с токеном бота
"""

import asyncio
import requests
from ttoken import TOKEN

BASE_URL = 'https://api.telegram.org/bot'

"""
После этого нам необходимо проверять есть ли у бота новые сообщения и в ответ отправлять это же сообщение пользователю, 
который отправил сообщение.
"""


def get_updates():
    r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
    message = r.json()['result'][-1]['message']['text']
    user_id = r.json()['result'][-1]['message']['chat']['id']
    requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')


get_updates()


"""
В данном коде мы отправляем запрос по ссылке согласно  документации, состоящей из адреса api, токена и названия метода. 
Для получения сообщений мы используем getUpdates. В переменную r мы сохраняем ответ сервера и в дальнейшем разбираем на 
необходимые нам составляющие: сообщение и пользователя отправившего его. 
После получения необходимых данных мы отправляем запрос используя в адресе метод sendMessage, 
который имеет обязательные параметры chat_id и text.

Данный код срабатывает один раз, так как у нас не реализованы, какие либо циклы позволяющие проверять данные постоянно. 
"""
