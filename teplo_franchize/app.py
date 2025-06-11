import logging

from aiogram import executor
from db import init, on_shutdown
from handlers import dp
from handlers.users.help import check
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    await init()
    await on_startup_notify(dp)
    print('Бот запущен')
    await set_default_commands(dp)
    await dp.bot.delete_webhook()
    await check()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


