"""
Давайте реализуем простой пример бота с учетом изученных нами фильтров.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}")


@dp.message_handler(CommandHelp())
async def bot_start(message: types.Message):
    await message.answer(f"{message.from_user.full_name}, вам нужна помощь?")


@dp.message_handler(Text(startswith='Бот'))
async def bot_start(message: types.Message):
    await message.answer(f"ВЫ ВВЕЛИ ТЕКСТ НАЧИНАЮЩИЙСЯ НА БОТ")


@dp.message_handler(Text(equals='телеграм'))
async def bot_start(message: types.Message):
    await message.answer(f"ВЫ ВВЕЛИ слово телеграмм")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
