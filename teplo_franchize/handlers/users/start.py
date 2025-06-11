import time

from aiogram import types
from aiogram.dispatcher import FSMContext

from db import Users, UsersData, TimeUsers, UserFlag
from handlers.users.help import questionnarium
from keyboards import StartIKB
from loader import dp
from state import QuestionnaireState


@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    if await Users.filter(tg_id=m.from_user.id).first() is None:
        await Users.create(tg_id=m.from_user.id)
    await m.answer('Открой свой табачный магазин по франшизе TEPLO и зарабатывай от 150.000 рублей в месяц!',
                   reply_markup=StartIKB.ikb)
    await m.answer("Бот создан командой @dDevLabs")


@dp.callback_query_handler(text="write_data")
async def write_data(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer(questionnarium["name"])
    await state.set_state(QuestionnaireState.name.state)


@dp.message_handler(state=QuestionnaireState.name)
async def name(m: types.Message, state: FSMContext):
    await state.update_data(name=m.text)
    await m.answer(questionnarium["contact_phone"])
    await state.set_state(QuestionnaireState.contact_phone.state)


@dp.message_handler(state=QuestionnaireState.contact_phone)
async def contact_phone(m: types.Message, state: FSMContext):
    await state.update_data(contact_phone=m.text)
    await m.answer(questionnarium["city_life"])
    await state.set_state(QuestionnaireState.city_life.state)


@dp.message_handler(state=QuestionnaireState.city_life)
async def city_life(m: types.Message, state: FSMContext):
    await state.update_data(city_life=m.text)
    await m.answer(questionnarium["city_open"])
    await state.set_state(QuestionnaireState.city_open.state)


@dp.message_handler(state=QuestionnaireState.city_open)
async def city_open(m: types.Message, state: FSMContext):
    await state.update_data(city_open=m.text)
    await m.answer(questionnarium["addition_info"])
    await state.set_state(QuestionnaireState.addition_info.state)


@dp.message_handler(state=QuestionnaireState.addition_info)
async def addition_info(m: types.Message, state: FSMContext):
    await state.update_data(addition_info=m.text)
    c_d = await state.get_data()

    message = f"@{m.from_user.username}\n\n" \
              f"1. Имя: {c_d['name']}\n" \
              f"2. Контактный номер: {c_d['contact_phone']}\n" \
              f"3. Город проживания: {c_d['city_life']}\n" \
              f"4. Город открытия: {c_d['city_open']}\n" \
              f"5. Дополнительная информация: {c_d['addition_info']}"

    await state.finish()
    await dp.bot.send_message(913406182, message)
    await m.answer("📩Ваша анкета отправлена франчайзинг-менеджеру!\n\n"
                   "🔻Анкеты обрабатываются ежедневно с 10:00 до 19:00 по местному времени.\n\n"
                   "🔻После обработки с вами свяжется наш франчайзинг-менеджер!\n\n"
                   "❗️Нам важно, чтобы вы не остались без внимания - поэтому по истечению 24 часов, вам придет мини-опрос о работе специалиста!")
    await UsersData.filter(tg_id=m.from_user.id).delete()
    await UsersData.create(tg_id=m.from_user.id,
                           name=c_d['name'],
                           contact_phone=c_d['contact_phone'],
                           city_life=c_d['city_life'],
                           city_open=c_d['city_open'],
                           addition_info=c_d['addition_info'])
    await TimeUsers.filter(tg_id=m.from_user.id).delete()
    await UserFlag.filter(tg_id=m.from_user.id).delete()
    await TimeUsers.create(tg_id=m.from_user.id,
                           time_int=time.time())


@dp.callback_query_handler(text="response:yes")
async def response_yes(c: types.CallbackQuery):
    await c.message.answer("👏 Здорово! Рады сотрудничеству")


@dp.callback_query_handler(text="response:no")
async def response_no(c: types.CallbackQuery):
    await c.message.answer("⚠️Нам очень жаль, что так вышло. Сейчас же передадим твою заявку вновь!")
    db_user = await UsersData.filter(tg_id=c.from_user.id).first()

    message = f"С @{c.from_user.username} не связались, а прошло больше 24 часов!\n\n" \
              f"1. Имя: {db_user.name}\n" \
              f"2. Контактный номер: {db_user.contact_phone}" \
              f"3. Город проживания: {db_user.city_life}" \
              f"4. Город открытия: {db_user.city_open}" \
              f"5. Дополнительная информация: {db_user.addition_info}"

    await dp.bot.send_message(1693556789, message)
