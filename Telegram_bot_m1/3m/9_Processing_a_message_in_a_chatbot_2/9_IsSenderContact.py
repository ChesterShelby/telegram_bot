"""
IsSenderContact - этот фильтр проверяет, что пользователь отправил именно свой контакт.
Может использоваться как callable или как аргумент is_sender_contact.
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import filters

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types='contact', is_sender_contact=True)
@dp.message_handler(filters.IsSenderContact(True), content_types='contact')
async def sender_contact_example(msg: types.Message):
    await msg.answer('Это вы')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
