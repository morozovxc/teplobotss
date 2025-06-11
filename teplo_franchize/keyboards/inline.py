from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class StartIKB:
    btn1 = InlineKeyboardButton(text="Изучить информацию", url="https://xn--80aanjeqpghmr2a9c.xn--p1ai/")
    btn2 = InlineKeyboardButton(text="Заполнить данные", callback_data="write_data")
    ikb = InlineKeyboardMarkup(1).add(btn1, btn2)


class DaysLeft:
    btn1 = InlineKeyboardButton(text="Да", callback_data="response:yes")
    btn2 = InlineKeyboardButton(text="Нет", callback_data="response:no")
    ikb = InlineKeyboardMarkup(2).add(btn1, btn2)
