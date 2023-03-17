import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'

logging.basicConfig(level=logging.INFO)
proxy_url = 'http://proxy.server:3128'
bot = Bot(token=API_TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    await message.answer('Вы ввели команду /start')
    print('hello')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
