import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

"""Создадим константы, которые нам потребуются"""

API_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'

# # настройки вебхука
# WEBHOOK_HOST = 'https://your.domain'
# WEBHOOK_PATH = '/path/to/api'
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
#
# # настройки веб сервера
# WEBAPP_HOST = 'localhost'
# WEBAPP_PORT = 3001

"""
WEBHOOK_HOST - в данной переменной мы указываем адрес вашего сервера
WEBHOOK_PATH - путь до api, где слушает бот
WEBHOOK_URL - в данной переменной формируется адрес необходимый url адрес, на который будут приниматься запросы
WEBAPP_HOST - хост нашего приложения, оставляем локальный
WEBAPP_PORT – порт, на котором работает наше приложение

"""  # настройки вебхуков
WEBHOOK_HOST = 'https://8e6d-85-193-108-171.ap.ngrok.io'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# настроки веб сервера
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 8082

"""
Так, с этим разобрались. Пойдем дальше и создадим объекты бота и диспетчера, а также укажем уровень логированния
"""

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

"""Создадим несколько функций on_startup и on_shutdown"""


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')


"""
Асинхронная функция on_startup устанавливает вебхук для нашего телеграм бота, на который будут отсылаться уведомления о получении новых сообщений.
on_shutdown, наоборот, удаляет этот вебхук при выключении и выводит соответствующий текст в логи.

Теперь давайте создадим обычный обработчик сообщений для бота реагирующего на команды start и help
"""


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    return SendMessage(message.chat.id, message.text)


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    return SendMessage(message.chat.id, 'Вы обратились к справке бота')


"""Готово! ну и теперь непосредственно укажем, что необходимо запускать не пуллинг, а вебхуки"""

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
