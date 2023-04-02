"""
ForwardedMessageFilter - этот фильтр проверяет, что отправленное сообщение является пересланным.
Может использоваться как аргумент is_forwarded или как объект класса.

Пусть бот ругает пользователя, за попытку отправить чужое сообщение
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import filters

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(is_forwarded=True)
@dp.message_handler(filters.ForwardedMessageFilter(True))
async def forwarded_example(msg: types.Message):
    await msg.answer('Не пытайся меня обмануть, я же вижу, что это не твоё сообщение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
