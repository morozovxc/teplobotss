from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Cross:
    btn1 = InlineKeyboardButton(text="НАЛИЧИЕ В МАГАЗИНЕ | ПРЕДЗАКАЗ", url="https://t.me/TEPLOINFOBOT")
    btn2 = InlineKeyboardButton(text="ХОЧУ В КОМАНДУ", url="https://t.me/TEPLOHRBOT")
    btn3 = InlineKeyboardButton(text="КУПИТЬ ФРАНШИЗУ", url="https://t.me/TEPLOFRANCHISEBOT")
    ikb = InlineKeyboardMarkup(1).add(btn1, btn2, btn3)
