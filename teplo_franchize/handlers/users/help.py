import time

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from db import TimeUsers, UserFlag
from keyboards import DaysLeft
from loader import dp


questionnarium: dict = {
    "name": "1. Введите Ваше имя:",
    "contact_phone": "2. Введите Ваш контактный номер:",
    "city_life": "3. Введите Ваш город проживания:",
    "city_open": "4. А в каком городе Вы планируете открыть франшизу?",
    "addition_info": "5. Введите дополнительную информацию:",
}


async def check_sched():
    for item in await TimeUsers.filter().all():
        if int(time.time()) - int(item.time_int) > 86400:

            if await UserFlag.filter(tg_id=item.tg_id).first() is None:
                await dp.bot.send_message(item.tg_id, "Ого! Ты написал анкету больше 24 часов назад, с тобой связался наш менеджер?",
                                          reply_markup=DaysLeft.ikb)
                await UserFlag.create(tg_id=item.tg_id)


async def check():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_sched, 'interval', minutes=5)
    scheduler.start()
