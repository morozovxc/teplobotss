from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class StartIKB:
    btn1 = InlineKeyboardButton(text="Давай", callback_data="go_quests")
    btn2 = InlineKeyboardButton(text="В другой раз", url="https://t.me/TEPLOINFOBOT")
    ikb = InlineKeyboardMarkup(2).add(btn1, btn2)

class DaysLeft:
    btn1 = InlineKeyboardButton(text="Да", callback_data="response:yes")
    btn2 = InlineKeyboardButton(text="Нет", callback_data="response:no")
    ikb = InlineKeyboardMarkup(2).add(btn1, btn2)
