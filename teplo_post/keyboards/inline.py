from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Cross:
    btn1 = InlineKeyboardButton(text="НАЛИЧИЕ В МАГАЗИНЕ | ПРЕДЗАКАЗ", url="https://t.me/TEPLOINFOBOT")
    btn2 = InlineKeyboardButton(text="ХОЧУ В КОМАНДУ", url="https://t.me/TEPLOHRBOT")
    btn3 = InlineKeyboardButton(text="КУПИТЬ ФРАНШИЗУ", url="https://t.me/TEPLOFRANCHISEBOT")
    btn4 = InlineKeyboardButton(text="ПОЛУЧИТЬ БОНУСНУЮ КАРТУ", url="https://t.me/TEPLOSTORESBOT")
    ikb = {
        'Наличие' : InlineKeyboardMarkup(1).add(btn1),
        'Команда' : InlineKeyboardMarkup(1).add(btn2),
        'Франшиза' : InlineKeyboardMarkup(1).add(btn3),
        'Бонусная карта' : InlineKeyboardMarkup(1).add(btn4),
        'Наличие + Команда' : InlineKeyboardMarkup(1).add(btn1, btn2),
        'Наличие + Франшиза' : InlineKeyboardMarkup(1).add(btn1, btn3),
        'Команда + Франшиза' : InlineKeyboardMarkup(1).add(btn2, btn3),
        'Все кнопки' : InlineKeyboardMarkup(1).add(btn1, btn2, btn3)
    }