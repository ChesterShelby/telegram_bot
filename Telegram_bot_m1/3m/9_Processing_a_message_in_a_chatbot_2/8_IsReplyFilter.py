"""
IsReplyFilter - один из простейших фильтров. Он проверит, является ли сообщение или пост в канале ответом.
Может использоваться как аргумент is_reply.
Допустим по команде user_id пусть бот возвращает ID пользователя, ответом на сообщение которого была использована команда.
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import filters

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(is_reply=True, commands='user_id')
@dp.message_handler(filters.IsReplyFilter(True), commands='user_id')
async def reply_filter_example(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
