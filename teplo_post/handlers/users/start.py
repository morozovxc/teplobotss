from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import admin_id
from keyboards import Cross
from loader import dp
from state import CreatePost


@dp.message_handler(commands=['start'])
@dp.message_handler(commands=['start'], state=CreatePost.states)
async def start(m: types.Message, state: FSMContext):
    await state.finish()
    if m.from_user.id in admin_id:
        await m.answer("Введите текст поста, без премиальных эмодзи и форматирования:")
        await state.set_state(CreatePost.text.state)


@dp.message_handler(state=CreatePost.text)
async def text(m: types.Message, state: FSMContext):
    await state.update_data(text=m.text)
    await m.answer("Отправьте одну картинку или видео для поста:")
    await state.set_state(CreatePost.photo.state)


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=CreatePost.photo)
@dp.message_handler(content_types="photo", state=CreatePost.photo)
async def photo(m: types.Message, state: FSMContext):
    try:
        await state.update_data(photo=m.photo[-1].file_id)
        c_d = await state.get_data()
        await dp.bot.send_photo(chat_id=-1001478749732,
                                photo=m.photo[-1].file_id,
                                caption=c_d["text"],
                                reply_markup=Cross.ikb)
        await m.answer(f"Сообщение опубликовано!")
        await state.finish()
    except Exception as e:
        await m.answer(f"Bad request!\n\n{e}")

@dp.message_handler(content_types=types.ContentTypes.VIDEO, state=CreatePost.photo)
@dp.message_handler(content_types="video", state=CreatePost.photo)
async def photo(m: types.Message, state: FSMContext):
    try:
        await state.update_data(photo=m.video.file_id)
        c_d = await state.get_data()
        await dp.bot.send_video(chat_id=-1001478749732,
                                video=m.video.file_id,
                                caption=c_d["text"],
                                reply_markup=Cross.ikb)
        await m.answer(f"Сообщение опубликовано!")
        await state.finish()
    except Exception as e:
        await m.answer(f"Bad request!\n\n{e}")
