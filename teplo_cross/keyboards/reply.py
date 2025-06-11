from aiogram import types


def ikb_main_menu():
    kb_main_city = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton(text="Открыть меню📕")
    kb_main_city.add(btn1)
    btn2 = types.KeyboardButton(text="Избранное🌟")
    btn3 = types.KeyboardButton(text="Корзина🛒")
    kb_main_city.add(btn2, btn3)
    return kb_main_city
