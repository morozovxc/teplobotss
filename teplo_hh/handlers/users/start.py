import datetime
import time

from aiogram import types
from aiogram.dispatcher import FSMContext

from db import Users, TimeUsers, UsersData, UserFlag
from handlers.users.help import questionnarium
from keyboards import StartIKB
from loader import dp
from state import QuestionnaireState
from keyboards import button_change


@dp.message_handler(commands=['start'])
@dp.message_handler(commands=['start'], state=QuestionnaireState.states)
async def start(m: types.Message, state: FSMContext):
    if await Users.filter(tg_id=m.from_user.id).first() is None:
        await Users.create(tg_id=m.from_user.id)
    await state.finish()
    await m.answer_photo(photo="https://7bdd6e9d-5639-4742-b439-36560b2a5ee9.selstorage.ru/hr_start.jpg",
                         caption="TEPLO - стремительно растёт и поэтому мы нуждаемся в постоянном наборе кадров!\n\n"
                                 "Давай заполним короткую анкету:", reply_markup=StartIKB.ikb)


@dp.callback_query_handler(text="go_quests")
async def go_quests(c: types.CallbackQuery, state: FSMContext):
    await state.set_state(QuestionnaireState.name.state)
    await c.message.answer(questionnarium["name"])


@dp.message_handler(state=QuestionnaireState.name)
async def name(m: types.Message, state: FSMContext):
    await state.update_data(name=m.text)
    await state.set_state(QuestionnaireState.contact_number.state)
    await m.answer(questionnarium["contact_number"])


@dp.message_handler(state=QuestionnaireState.contact_number)
async def contact_number(m: types.Message, state: FSMContext):
    await state.update_data(contact_number=m.text)
    await state.set_state(QuestionnaireState.square.state)
    await m.answer(questionnarium["square"])

@dp.message_handler(state=QuestionnaireState.square)
async def square(m: types.Message, state: FSMContext):
    await state.update_data(square=m.text)
    await state.set_state(QuestionnaireState.place_of_residence.state)
    await m.answer(questionnarium["place_of_residence"])


@dp.message_handler(state=QuestionnaireState.place_of_residence)
async def place_of_residence(m: types.Message, state: FSMContext):
    await state.update_data(place_of_residence=m.text)
    await state.set_state(QuestionnaireState.date_of_birth.state)
    await m.answer(questionnarium["date_of_birth"])


@dp.message_handler(state=QuestionnaireState.date_of_birth)
async def date_of_birth(m: types.Message, state: FSMContext):
    # Получаем дату рождения из сообщения
    date_str = str(m.text)
    try:
        # Разделяем строку даты на части
        parts = date_str.split('.')

        # Преобразуем части строки в целые числа
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError as e:
        # Если дата введена неправильно, выводим сообщение об ошибке
        await m.answer(f'Неверный формат даты: {e}')
        await state.finish()
        return

    from datetime import date

    # Текущая дата
    current_date = date.today()

    # Дата рождения пользователя
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    birth_date = date(year, month, day)

    # Вычисление возраста
    age = current_date.year - birth_date.year

    # Учет месяцев и дней
    if birth_date.month > current_date.month or \
            (birth_date.month == current_date.month and birth_date.day > current_date.day):
        age -= 1

    # Проверка возраста
    if age < 18:
        await m.answer('К сожалению, вам ещё нет 18-ти лет, возвращайтесь сразу как исполнится)')
        await state.finish()
        return

    # Если все проверки пройдены, продолжаем выполнение программы
    await state.update_data(date_of_birth=m.text)
    await state.set_state(QuestionnaireState.criminal.state)
    await m.answer(questionnarium["criminal"])


#@dp.message_handler(state=QuestionnaireState.minor_children)
#async def minor_children(m: types.Message, state: FSMContext):
#    await state.update_data(minor_children=m.text)
 #   await state.set_state(QuestionnaireState.criminal.state)
  #  await m.answer(questionnarium["criminal"])


@dp.message_handler(state=QuestionnaireState.criminal)
async def criminal(m: types.Message, state: FSMContext):
    await state.update_data(criminal=m.text)
    await state.set_state(QuestionnaireState.education.state)
    await m.answer(questionnarium["education"])


@dp.message_handler(state=QuestionnaireState.education)
async def education(m: types.Message, state: FSMContext):
    await state.update_data(education=m.text)
    await state.set_state(QuestionnaireState.russian_citizenship.state)
    await m.answer(questionnarium["russian_citizenship"])

@dp.message_handler(state=QuestionnaireState.russian_citizenship)
async def russian_citizenship(m: types.Message, state: FSMContext):
    await state.update_data(russian_citizenship=m.text)
    await state.set_state(QuestionnaireState.comment.state)
    await m.answer(questionnarium["comment"], reply_markup=button_change())

@dp.message_handler(state=QuestionnaireState.comment)
async def comment(m: types.Message, state: FSMContext):
    await state.update_data(comment=m.text)
    c_d = await state.get_data()
    await state.set_state(QuestionnaireState.comment_save.state)
    if m.text == 'Нет':
        c_d['comment_save'] = 'Без комментария'
        await send(m, c_d)
    else:
        await m.answer(questionnarium["comment_save"])


@dp.message_handler(state=QuestionnaireState.comment_save)
async def comment_save(m: types.Message, state: FSMContext):
    await state.update_data(comment_save=m.text)
    c_d = await state.get_data()

    if c_d['comment'] == 'Нет':
        c_d['comment_save'] = 'Без комментария'

    await send(m, c_d)
    await state.finish()

async def send(m: types.Message, c_d):
    message = f"@{m.from_user.username}\n\n" \
        f"1. Имя: {c_d['name']}\n" \
        f"2. Контактный номер: {c_d['contact_number']}\n" \
        f"3. Желаемый район работы: {c_d['square']}\n" \
        f"4. Место жительства: {c_d['place_of_residence']}\n" \
        f"5. Дата рождения: {c_d['date_of_birth']}\n" \
        f"6. Судимость: {c_d['criminal']}\n" \
        f"7. Образование: {c_d['education']}\n" \
        f"8. Гражданство РФ: {c_d['russian_citizenship']}\n" \
        f"9. Комментарий: {c_d['comment_save']}"

    await dp.bot.send_message(875572761, message)
    await m.answer("🎯Ваша анкета отправлена HR-менеджеру!\n\n"
                   "🔻Анкеты обрабатываются ежедневно с 10:00 до 19:00 по местному времени.\n\n"
                   "🔻После обработки с вами свяжется наш HR-менеджер.\n\n"
                   "❗️Нам важно, чтобы вы не остались без внимания - поэтому по истечению 24 часов, вам придет мини-опрос о работе специалиста!")
    await UsersData.filter(tg_id=m.from_user.id).delete()
    await UsersData.create(tg_id=m.from_user.id,
                           name=c_d['name'],
                           contact_number=c_d['contact_number'],
                           square=c_d['square'],
                           place_of_residence=c_d['place_of_residence'],
                           date_of_birth=c_d['date_of_birth'],
                           criminal=c_d['criminal'],
                           education=c_d['education'],
                           russian_citizenship=c_d['russian_citizenship'],
                           comment=c_d['comment'],
                           comment_save=c_d['comment_save'])
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
              f"2. Контактный номер: {db_user.contact_number}\n" \
              f"3. Желаемое место работы: {db_user.square}\n" \
              f"4. Место жительства: {db_user.place_of_residence}\n" \
              f"5. Дата рождения: {db_user.date_of_birth}\n" \
              f"6. Судимость: {db_user.criminal}\n" \
              f"7. Образование: {db_user.education}\n" \
              f"8. Гражданство РФ: {db_user.russian_citizenship}\n" \
              f"9. Комментарий: {db_user.comment_save}"

    await dp.bot.send_message(875572761, message)
