import logging

from aiogram import Dispatcher

from data.config import admin_ids


async def on_startup_notify(dp: Dispatcher):
    for admin in admin_ids:
        try:
            text = 'Бот запущен'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
