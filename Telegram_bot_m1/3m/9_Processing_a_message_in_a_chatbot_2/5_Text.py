"""
Text - Ещё один очень популярный фильтр. Он проверяет текст, будь это текст сообщения, или callback_data кнопки.
Кроме полной идентичности (equals), данный фильтр также может проверить то, что текст начинается,
содержит или заканчивается какой-либо строкой. Вы можете использовать импортированный класс,
передавая в него аргументы либо использовать фильтр как аргумент функции. Пройдёмся по аргументам конструктора класса:

equals — строка, которой текст должен быть идентичен
contains — строка, которую должен содержаться текст
startswith — строка, которой текст должен начинаться
endswith — строка, которой текст должен заканчиваться
ignore_case — игнорировать регистр текст. Проверяется с помощью str.lower().

Данный фильтр может использоваться как аргумент. Для этого используйте text, text_contains, text_startswith или text_endswith.
Рассмотрим следующий пример: допустим нам нужно отвечать в чате участнику за какую-нибудь фразу:
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import filters

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

FORBIDDEN_PHRASE = [
    'C++',
    'Python'
]


@dp.message_handler(filters.Text(contains=FORBIDDEN_PHRASE, ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Ответ!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


"""
Таким образом, если сообщение пользователя будет содержать обе строки из списка, бот ответит сообщением.
"""