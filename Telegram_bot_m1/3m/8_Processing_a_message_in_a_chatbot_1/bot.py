import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters

from config import BOT_TOKEN
from aiogram import types

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(filters.CommandStart(deep_link='deep_link'))
async def deep_link(msg: types.Message):
    await msg.answer('Да, знаем мы такое')


@dp.message_handler(filters.CommandStart())
async def command_start_handler(msg: types.Message):
    await msg.answer('Привет!')


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
