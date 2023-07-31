from aiogram import executor
import logging
from database.create_table import create_table
from settings import dp
from handlers.start import send_start_message
from handlers.add_phone import add_phone, get_phone_number
from handlers.limits import ask_limit, get_limit
from handlers.remove_phone import get_user_phone_numbers, remove_phone
from handlers.balances import get_all_balances


if __name__ == "__main__":
    logging.info("Create database table...")
    create_table()
    logging.info("Start telegram bot...")
    executor.start_polling(dp, skip_updates=True)
