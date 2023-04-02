"""
HashTag - Данный фильтр проверяет то, что в сообщении содержится определённый хеш (#) или кеш ($) тег.
Может использоваться либо как callable, либо как аргументы hashtags и cashtags.
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types


BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def hashtag_example(msg: types.Message):
    await msg.answer('Ееее, деньги 😎')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
