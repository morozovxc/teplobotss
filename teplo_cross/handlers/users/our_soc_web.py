from aiogram import types

from loader import dp
from keyboards import OurSocWeb


@dp.callback_query_handler(text_startswith="our_soc_web")
async def our_soc_web(c: types.CallbackQuery):
    m_id = str(c.data).split(":")[1]
    await dp.bot.edit_message_text(text=f"📱Социальные сети TEPLO\n\n"
                                        f"❗️Instagram*\n\n"
                                        f"*Продукт компании Meta, признан экстремистской организацией на территории РФ.",
                                   chat_id=c.from_user.id,
                                   message_id=m_id,
                                   reply_markup=await OurSocWeb.ikb(m_id=m_id))
