from aiogram import types

from keyboards import FRANCHISE
from loader import dp


@dp.callback_query_handler(text_startswith="go_to_FRANCHISE")
async def go_to_FRANCHISE(c: types.CallbackQuery):
    m_id = str(c.data).split(":")[1]
    await dp.bot.edit_message_text(text="🔥Открой свой табачный магазин по франшизе TEPLO, заполнив короткую анкету:",
                                   chat_id=c.from_user.id,
                                   message_id=m_id,
                                   reply_markup=await FRANCHISE.ikb(m_id=m_id))
