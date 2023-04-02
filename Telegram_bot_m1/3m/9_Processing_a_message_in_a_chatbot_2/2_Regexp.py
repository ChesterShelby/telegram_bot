"""
Фильтр, проверяющий регулярное выражение. Подключён на большинство обработчиков.
Для примера напишем обработчик, который будет обрабатывать ссылку на изображения:
"""

from aiogram.dispatcher import filters
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

IMAGE_REGEXP = r'https://.+?\.(jpg|png|jpeg)'


@dp.message_handler(filters.Regexp(IMAGE_REGEXP))
async def regexp_example(msg: types.Message):
    await msg.answer('Похоже на картинку, не так ли?')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    