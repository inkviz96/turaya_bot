from aiogram import types
import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.add_user import add_user
from messages_text import (
    message_added_number,
    message_error_number,
    message_input_phone,
)
from keyboards import main_keyboard
from handlers.utils import get_balance
from settings import dp


class GetPhoneForm(StatesGroup):
    waiting_for_phone = State()
    waiting_for_limit = State()


@dp.message_handler(lambda message: message.text == "➕ Добавить отслеживаемый номер")
async def add_phone(message: types.Message):
    await message.reply(message_input_phone, reply_markup=main_keyboard)
    await GetPhoneForm.waiting_for_phone.set()


@dp.message_handler(state=GetPhoneForm.waiting_for_phone)
async def get_phone_number(message: types.Message, state: FSMContext):
    phone = message.text
    balance = get_balance(phone)
    logging.info(balance)
    if phone.startswith("+882") and len(phone) == 14 and balance.status_code == 200:
        await message.answer(
            message_added_number.replace(
                "<balance>", balance.json()["balance"]
            ).replace("<data>", balance.json()["LastActiveDate"]),
            reply_markup=main_keyboard,
        )
        add_user(message.from_user.id, phone)
        logging.info(f"NEW_USER: ID: {message.from_user.id} PHONE: {phone}")
    else:
        await message.answer(message_error_number, reply_markup=main_keyboard)
    await state.finish()
