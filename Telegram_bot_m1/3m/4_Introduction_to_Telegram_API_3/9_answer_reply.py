"""
Более того, для большинства типов сообщений есть вспомогательные методы вида "answer_{type}" или "reply_{type}",
например:
"""

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from ttoken import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


if __name__ == '__main__':
    executor.start_polling(dp)
