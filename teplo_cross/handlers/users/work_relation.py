from aiogram import types

from loader import dp
from keyboards import *


@dp.callback_query_handler(text_startswith="work_relation")
async def work_relation(c: types.CallbackQuery):
    m_id = str(c.data).split(":")[1]
    await dp.bot.edit_message_text(text=f"🔎 Какое сотрудничество тебя интересует?",
                                   chat_id=c.from_user.id,
                                   message_id=m_id,
                                   reply_markup=await WorkRelation.ikb(m_id=m_id))


@dp.callback_query_handler(text_startswith="marketing")
async def marketing(c: types.CallbackQuery):
    m_id = str(c.data).split(":")[1]
    await dp.bot.edit_message_text(text=f"Андреева Кристина Андреевна - Директор по маркетингу компании TEPLO",
                                   chat_id=c.from_user.id,
                                   message_id=m_id,
                                   reply_markup=await MarketingBTN.ikb(m_id=m_id))


@dp.callback_query_handler(text_startswith="partnership")
async def partnership(c: types.CallbackQuery):
    m_id = str(c.data).split(":")[1]
    await dp.bot.edit_message_text(text=f"Койнов Артем Сергеевич - Директор отдела закупа компании TEPLO",
                                   chat_id=c.from_user.id,
                                   message_id=m_id,
                                   reply_markup=await PartnershipBTN.ikb(m_id=m_id))
