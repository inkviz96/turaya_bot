from redis_storage import RedisStorage
from aiogram import Bot, Dispatcher
import logging
import os


API_TOKEN = os.getenv("API_TOKEN")
BALANCE_URL = os.getenv("BALANCE_URL")

storage = RedisStorage("localhost", 6379, db=5, pool_size=10, prefix="my_fsm_key")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
