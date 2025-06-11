from aiogram import types

from db import Users
from keyboards import Start
from loader import dp


@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    if await Users.filter(tg_id=m.from_user.id).first() is None:
        await Users.create(tg_id=m.from_user.id)
    #await m.answer("Бот создан командой @dDevLabs")

    mes = await m.answer(f"🙋‍♀️Привет, @{m.from_user.username}\n\n"
                         f"Какой у тебя вопрос?")
    await dp.bot.edit_message_text(text=f"Привет, @{m.from_user.username}\n\n"
                                        f"Чем я могу тебе помочь?",
                                   chat_id=m.from_user.id,
                                   message_id=mes.message_id,
                                   reply_markup=await Start.start_ikb(m_id=mes.message_id))


@dp.callback_query_handler(text_startswith="total_back")
async def total_back(c: types.CallbackQuery):
    m_id = str(c.data).split(":")[1]
    await dp.bot.edit_message_text(text=f"Привет, @{c.from_user.username}\n\n"
                                        f"Чем я могу тебе помочь?",
                                   chat_id=c.from_user.id,
                                   message_id=m_id,
                                   reply_markup=await Start.start_ikb(m_id=m_id))

