from aiogram.dispatcher.filters.state import State, StatesGroup


class QuestionnaireState(StatesGroup):
    name = State()
    contact_phone = State()
    city_life = State()
    city_open = State()
    addition_info = State()