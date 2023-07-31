from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton


add_number = InlineKeyboardButton(
    text="➕ Добавить отслеживаемый номер", callback_data="add_number_phone"
)
remove_number = InlineKeyboardButton(
    text="➖ Удалить неактивный номер", callback_data="remove_number_phone"
)
balances = InlineKeyboardButton(
    text="🔍 Узнать баланс всех отслеживаемых номеров", callback_data="get_all_balances"
)
add_limit = InlineKeyboardButton(
    text="🚨 Установить сумму для оповещения", callback_data="add_unit_limit"
)

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.row(add_number)
main_keyboard.row(remove_number)
main_keyboard.row(balances)
main_keyboard.row(add_limit)
