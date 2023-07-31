import logging

from messages_text import message_add_limit, message_added_limit, message_wrong_limit
from database.get_limit import get_user_limit, change_limit
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import main_keyboard
from settings import dp


class LimitForm(StatesGroup):
    waiting_for_limit = State()


@dp.message_handler(lambda message: message.text == "🚨 Установить сумму для оповещения")
async def ask_limit(message: types.Message):
    await message.reply(message_add_limit, reply_markup=main_keyboard)
    await LimitForm.waiting_for_limit.set()


@dp.message_handler(state=LimitForm.waiting_for_limit)
async def get_limit(message: types.Message, state: FSMContext):
    limit = message.text
    if int(limit) < 10 or int(limit) > 1000 or not limit.isdigit():
        await message.answer(message_wrong_limit, reply_markup=main_keyboard)
    else:
        change_limit(message.from_user.id, limit)
        await message.answer(
            message_added_limit.replace("<limit>", limit), reply_markup=main_keyboard
        )

    await state.finish()
