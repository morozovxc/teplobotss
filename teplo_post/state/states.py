from aiogram.dispatcher.filters.state import State, StatesGroup


class CreatePost(StatesGroup):
    text = State()
    change = State()
    photo = State()