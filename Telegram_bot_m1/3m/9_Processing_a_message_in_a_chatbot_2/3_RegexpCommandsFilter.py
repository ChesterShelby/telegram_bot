"""
Этот фильтр может использоваться также и как аргумент. Используйте для этого ключевое слово regexp:

@dp.message_handler(regexp=IMAGE_REGEXP)
async def regexp_example(msg: types.Message):
. . .

RegexpCommandsFilter - Фильтр, проверяющий команду через регулярное выражение. Может использоваться как аргумент
regexp_commands (Именно поэтому у меня функция с двумя декораторами, вам стоит использовать один из приведенных вариантов).
Возьмём идентичный пример. Реализуем команду image с несколькими префиксами, которые проверяют ссылку на изображение:
"""

from aiogram.dispatcher import filters
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


IMAGE_REGEXP = r'https://.+?\.(jpg|png|jpeg)'
COMMAND_IMAGE_REGEXP = r"/image:" + IMAGE_REGEXP


@dp.message_handler(filters.RegexpCommandsFilter([COMMAND_IMAGE_REGEXP]))
@dp.message_handler(regexp_commands=[COMMAND_IMAGE_REGEXP])
async def command_regexp_example(msg: types.Message):
    await msg.answer('По вашей команде докладываю, что данная ссылка является изображением!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


"""
Изначально в фильтре идёт проверка на команду, так что сообщение должно начинаться с косой черты. 
"""
