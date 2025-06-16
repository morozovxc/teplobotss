from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types


class StartIKB:
    btn1 = InlineKeyboardButton(text="Давай", callback_data="go_quests")
    btn2 = InlineKeyboardButton(text="В другой раз", url="https://t.me/TEPLOINFOBOT")
    ikb = InlineKeyboardMarkup(2).add(btn1, btn2)

def button_change():
    kb_main_city = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton(text="Да")
    btn2 = types.KeyboardButton(text="Нет")
    kb_main_city.add(btn1, btn2)
    return kb_main_city

class DaysLeft:
    btn1 = InlineKeyboardButton(text="Да", callback_data="response:yes")
    btn2 = InlineKeyboardButton(text="Нет", callback_data="response:no")
    ikb = InlineKeyboardMarkup(2).add(btn1, btn2)
