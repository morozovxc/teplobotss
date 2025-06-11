import time

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from loader import dp
from aiogram import types
from db import TimeUsers, UserFlag
from keyboards import DaysLeft


questionnarium: dict = {
    "name": "1. Введите Ваше имя:",
    "contact_number": "2. Введите Ваш контактный номер:",
    "gender": "3. Введите Ваш пол:",
    "place_of_residence": "4. Введите Ваше место жительства (город, район, улица):",
    "date_of_birth": "5. Введите Вашу дату рождения в формате <b>ДД.ММ.ГГГГ</b>:",
    "minor_children": "6. Есть ли у Вас несовершеннолетние дети?",
    "criminal": "7. Есть ли у Вас судимость?",
    "education": "8. Есть ли у Вас образование. Если сейчас проходите обучение, укажите специальность и форму (очная/заочная)",
    "russian_citizenship": "9. У вас есть гражданство РФ?",
    "ready_to_job_officially": "10. Готовы трудоустроиться официально?"
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
