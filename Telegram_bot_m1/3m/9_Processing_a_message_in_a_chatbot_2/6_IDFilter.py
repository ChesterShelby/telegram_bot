"""
IDFilter - Ещё один фильтр, который заслуживает внимания — фильтр для проверки идентификатора.
Он может использоваться как аргумент user_id, chat_id, так и как callable объект IDFilter(user_id=12345789)

Сам фильтр имеет два аргумента:
user_id — проверяет ID пользователя
chat_id — проверяет ID чата

Представим, что нам нужно написать обработчик, который будет отвечать на все сообщения в диалоге с админом,
если обновление не попало ни в один из обработчиков (для этого расположим обработчик в конце файла).
Таким образом в конфигурационном файле у нас есть константа типа List с идентификаторами суперпользователей SUPERUSER_IDS.
Пример будет иметь следующий вид:
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import filters

from app.config import SUPERUSER_IDS

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(filters.IDFilter(chat_id=SUPERUSER_IDS))
@dp.message_handler(chat_id=SUPERUSER_IDS)
async def id_filter_example(msg: types.Message):
    await msg.answer('Да, помню тебя')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

"""
Этот обработчик сработает на сообщение суперпользователя, и только если ни это сообщение 
не прошло по фильтрам ни в один из предыдущих фильтров.
"""
