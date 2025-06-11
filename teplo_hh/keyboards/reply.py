from aiogram import types


def rkb_gender():
    kb_main_city = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton(text="Мужской")
    btn2 = types.KeyboardButton(text="Женский")
    kb_main_city.add(btn1, btn2)
    return kb_main_city
