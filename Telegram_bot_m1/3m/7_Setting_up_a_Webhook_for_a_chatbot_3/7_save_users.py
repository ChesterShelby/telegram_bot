"""
Наш бот будет проверять есть ли пользователь в базе данных. Если нет, то добавлять,
если есть, то выводить данные по нему. Сделаем заготовку
"""

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


@dp.message_handler(text='база')
async def echo(message: types.Message):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    user = cur.execute(f"""SELECT * FROM users WHERE userid = {message.chat.id}""").fetchone()
    if not user:
        print('NO')
    else:
        print("YES")
    await message.answer(message.text)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    create_table()
    executor.start_polling(dp, skip_updates=True)

# Запрос  cur.execute(f"""SELECT * FROM users WHERE userid = {message.chat.id}""").fetchone() позволяет получить пользователя,
# который написал сообщение, из указанной таблицы. Пока в таблице у нас никого нет.
# if not user: проверяет получен ли такой пользователь
