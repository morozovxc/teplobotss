from aiogram import types


def ikb_main_menu():
    kb_main_city = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton(text="Открыть меню📕")
    kb_main_city.add(btn1)
    btn2 = types.KeyboardButton(text="Избранное🌟")
    btn3 = types.KeyboardButton(text="Корзина🛒")
    kb_main_city.add(btn2, btn3)
    return kb_main_city

def button_change():
    kb_main_city = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton(text="Наличие")
    btn2 = types.KeyboardButton(text="Команда")
    btn3 = types.KeyboardButton(text="Франшиза")
    btn4 = types.KeyboardButton(text="Наличие + Команда")
    btn5 = types.KeyboardButton(text="Наличие + Франшиза")
    btn6 = types.KeyboardButton(text="Команда + Франшиза")
    btn7 = types.KeyboardButton(text="Все кнопки")
    kb_main_city.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return kb_main_city