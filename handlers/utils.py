import requests
from requests import Response
from settings import BALANCE_URL
import logging
from settings import bot
import asyncio
from database.get_all_users import get_all_users
from database.get_limit import get_user_limit
from messages_text import message_low_balance, message_pay_day
from datetime import datetime, timedelta
from database.get_limit_alert import get_limit_alert
from database.update_limit_alert import change_limit_alert


def get_balance(number: str) -> Response:
    return requests.get(url=f"{BALANCE_URL}{number}")


async def check_balances() -> None:
    users = get_all_users()
    if not users:
        return
    for _, tg_id, phone in users:
        limit = get_user_limit(tg_id)
        balance = get_balance(phone)
        logging.info(
            f"ID: {tg_id}, {phone} - {balance.json()['balance']}, [{balance.json()['LastActiveDate']}]"
        )
        last_update = get_limit_alert(tg_id, phone)
        if float(balance.json()["balance"]) < int(limit[0]) and (
            last_update
            or datetime.fromtimestamp(last_update) + timedelta(days=7) > datetime.now()
        ):
            await bot.send_message(
                int(tg_id),
                message_low_balance.replace("<phone>", phone).replace(
                    "<balance>", balance.json()["balance"]
                ),
            )
            change_limit_alert(tg_id, str(datetime.now().timestamp()), phone)
        await asyncio.sleep(1)


async def check_data() -> None:
    users = get_all_users()
    if not users:
        return
    for _, tg_id, phone in users:
        response = get_balance(phone)
        if response.json()["LastActiveDate"] + timedelta(days=30) >= datetime.now():
            await bot.send_message(
                int(tg_id),
                message_pay_day.replace("<phone>", phone)
                .replace("<balance>", response.json()["balance"])
                .replace("<data>", response.json()["LastActiveDate"]),
            )
