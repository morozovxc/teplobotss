from aiogram.dispatcher.filters.state import State, StatesGroup


class QuestionnaireState(StatesGroup):
    name = State()
    contact_number = State()
    square = State()
    place_of_residence = State()
    date_of_birth = State()
    criminal = State()
    education = State()
    russian_citizenship = State()