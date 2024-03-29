"""
Хэндлер cmd_test2 не сработает, т.к. диспетчер о нём не знает. Исправим эту ошибку и отдельно зарегистрируем функцию:
"""

import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from ttoken import TOKEN

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher(bot)


# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# Хэндлер на команду /test1
@dp.message_handler(commands=["test1"])
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


dp.register_message_handler(cmd_test2, commands="test2")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
