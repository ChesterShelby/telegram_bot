"""
Python является интерпретируемым языком с сильной, но динамической типизацией, поэтому встроенная проверка типов,
как, например, в C++ или Java, отсутствует. Однако начиная с версии 3.5 в языке появилась поддержка подсказок типов,
благодаря которой различные чекеры и IDE вроде PyCharm анализируют типы используемых значений и подсказывают программисту,
если он передаёт что-то не то. В данном случае подсказка types.Message соообщает PyCharm-у,
что переменная message имеет тип Message, описанный в модуле types библиотеки aiogram.
Благодаря этому IDE может на лету подсказывать атрибуты и функции.

При вызове команды /dice бот отправит в тот же чат игральный кубик. Разумеется,
если его надо отправить в какой-то другой чат, то придётся по-старинке вызывать await bot.send_dice(...).
Но объект bot (экземпляр класса Bot) может быть недоступен в области видимости конкретной функции.
К счастью, объект бота доступен во всех типах апдейтов: Message, CallbackQuery, InlineQuery и т.д. Предположим,
вы хотите по команде /dice отправлять кубик не в тот же чат, а в канал с ID -898429236. Перепишем предыдущую функцию:

"""

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from os import getenv
from sys import exit


bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.bot.send_dice(-898429236, emoji="🎲")


if __name__ == '__main__':
    executor.start_polling(dp)
