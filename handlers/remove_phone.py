from settings import dp
from database.get_user import get_user_phones, delete_phone
import itertools
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from messages_text import (
    message_error_number,
    message_remove_number,
    message_choice_phone,
    message_not_phone,
)
from keyboards import main_keyboard
from aiogram import types
import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RemovePhoneForm(StatesGroup):
    waiting_for_phone = State()


@dp.message_handler(lambda message: message.text == "➖ Удалить неактивный номер")
async def get_user_phone_numbers(message: types.Message):
    phones = "\n".join(
        [
            phone
            for phone in itertools.chain.from_iterable(
                get_user_phones(message.from_user.id)
            )
        ]
    )
    buttons = []
    for phone in phones.split("\n"):
        buttons.append(InlineKeyboardButton(text=f"{phone}", callback_data=f"{phone}"))
    keyboard_inline = ReplyKeyboardMarkup().add(*buttons)
    if not phones:
        await message.reply(message_not_phone, reply_markup=main_keyboard)
    else:
        await message.reply(message_choice_phone, reply_markup=keyboard_inline)
        await RemovePhoneForm.waiting_for_phone.set()


@dp.message_handler(state=RemovePhoneForm.waiting_for_phone)
async def remove_phone(message: types.Message, state: FSMContext):
    phone = message.text
    phones = get_user_phones(message.from_user.id)
    if (phone,) not in phones:
        await message.answer(message_error_number, reply_markup=main_keyboard)
    else:
        delete_phone(message.from_user.id, phone)
        await message.answer(message_remove_number, reply_markup=main_keyboard)
        logging.info(f"User {message.from_user.id} removed phone {phone}")
    await state.finish()
