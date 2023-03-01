from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# from ttoken import TOKEN
TOKEN = '6128647054:AAGdU2hOxoOC-7Sx5wzad3ySeDVbQtUy9Gk'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
