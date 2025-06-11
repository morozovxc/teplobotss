from aiogram.dispatcher.filters.state import State, StatesGroup


class CreatePost(StatesGroup):
    text = State()
    photo = State()