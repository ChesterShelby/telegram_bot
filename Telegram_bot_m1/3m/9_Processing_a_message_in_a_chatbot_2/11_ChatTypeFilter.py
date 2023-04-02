"""
ChatTypeFilter - Из названия этого фильтра понятно, что он проверяет тип чата. Он может использоваться либо как объект,
либо как аргумент chat_type. Принимает либо строку, либо types.ChatType (что тоже является строкой).
Допустим нам нужно, чтобы бот по команде is_pm подтверждал, что команда выполнена в личных сообщениях.
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import filters

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(chat_type=types.ChatType.PRIVATE, commands='is_pm')
@dp.message_handler(chat_type='private', commands='is_pm')
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='is_pm')
async def chat_type_example(msg: types.Message):
    await msg.answer('Да, это личные сообщения')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
