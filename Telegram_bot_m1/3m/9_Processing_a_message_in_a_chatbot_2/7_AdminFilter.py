"""
AdminFilter - Один из любимых фильтров разработчиков чат модераторов. Как понятно из названия проверяет,
что запрос прилетел от администратора чата. Может использоваться как callable объект, или аргумент функции.
Допустим мы пишем бота для администрирования чата и нам нужна команда, для изменения изображения чата.
Естественно, такую команду не следует доверять обычным пользователям,
поэтому пусть ответственность за использование этой команды будет исключительно на плечах администрации чата
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import filters

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='change_photo', is_chat_admin=True)
@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def chat_admin_example(msg: types.Message):
    await msg.answer('Нет')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

"""
Тут используются два декоратора исключительно для демонстрации. Вам стоит выбрать одно из решений. Также обратите внимание, 
что вперёд стоит фильтр на команду, потому что AdminFilter делает запрос в API, что требует времени, а значит замедляет работу бота.
Кроме логического типа данных, этот фильтр может также содержать ID чата. В этом случае он будет проверять, 
что запрос пришел именно от администратора чата с конкретным идентификатором, а не текущего чата.
Этот фильтр не может быть False.
Если при использовании этого фильтра как callable не передавать аргументы, проверяться будет администрация текущего чата.
"""
