from settings import dp
from aiogram import types
from messages_text import start_message
from keyboards import main_keyboard


@dp.message_handler(commands=["start"])
async def send_start_message(message: types.Message):
    await message.reply(start_message, reply_markup=main_keyboard)
