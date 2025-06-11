from aiogram.dispatcher.filters.state import State, StatesGroup


class QuestionnaireState(StatesGroup):
    name = State()
    contact_number = State()
    gender = State()
    place_of_residence = State()
    date_of_birth = State()
    minor_children = State()
    criminal = State()
    education = State()
    russian_citizenship = State()
    ready_to_job_officially = State()