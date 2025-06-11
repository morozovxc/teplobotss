from aiogram import types

from loader import dp


@dp.message_handler(commands=['help'])
async def start(m: types.Message):
    await m.answer('help')
