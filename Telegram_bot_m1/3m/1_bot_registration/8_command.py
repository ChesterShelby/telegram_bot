from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from ttoken import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

"""
В данном случае стоит учитывать, что если указать хендлер, который перехватывает все сообщения, выше чем остальные, 
то остальные хендлеры не будут работать. 

Вот таким образом мы посмотрели как взаимодействовать с API телеграмм с помощью модуля и без
"""
