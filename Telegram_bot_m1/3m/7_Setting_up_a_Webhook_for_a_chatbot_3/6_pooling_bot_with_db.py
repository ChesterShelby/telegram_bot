"""Вернемся к локальному эхо боту  с пуллингом из прошлых уроков создадим в боте таблицу"""

import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def create_table():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               username TEXT,
               message TEXT);
               """)
    conn.commit()
    cur.close()
    conn.close()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Вы ввели одну из команд.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    create_table()
    executor.start_polling(dp, skip_updates=True)
