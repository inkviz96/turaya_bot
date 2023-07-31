from aiogram import types
from settings import dp
from database.get_user import get_user_phones
import itertools
from messages_text import message_balances, message_balance_without_phone
from keyboards import main_keyboard
from handlers.utils import get_balance


@dp.message_handler(
    lambda message: message.text == "🔍 Узнать баланс всех отслеживаемых номеров"
)
async def get_all_balances(message: types.Message):
    phones = "\n".join(
        [
            phone
            for phone in itertools.chain.from_iterable(
                get_user_phones(message.from_user.id)
            )
        ]
    )
    if not phones:
        await message.reply(message_balance_without_phone, reply_markup=main_keyboard)
    for phone in phones.split("\n"):
        balance = get_balance(phone)
        await message.reply(
            message_balances.replace("<phone>", phone)
            .replace("<balance>", balance.json()["balance"])
            .replace("<data>", balance.json()["LastActiveDate"]),
            reply_markup=main_keyboard,
        )
