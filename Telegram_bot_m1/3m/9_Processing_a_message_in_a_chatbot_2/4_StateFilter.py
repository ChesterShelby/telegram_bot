"""
StateFilter - Этот фильтр проверяет состояние, в котором находится пользователь.
Он может использоваться только как аргумент функции state. Для примера опишем 2 обработчика:
для присвоения состояния и для его сброса.
"""

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import FSMContext

BOT_TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='set_state')
async def set_state(msg: types.Message, state: FSMContext):
    """Присваиваем пользователю состояние для теста"""
    await state.set_state('example_state')
    await msg.answer('Состояние установлено')


@dp.message_handler(state='example_state')
async def state_example(msg: types.Message, state: FSMContext):
    await msg.answer('Ой всё, иди отсюда')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
