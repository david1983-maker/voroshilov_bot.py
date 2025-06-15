from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class SizeState(StatesGroup):
    dlina = State()
    shirina = State()
    visota = State()
    potolok = State()


class TasteState(StatesGroup):
    form = State()
    island = State()
    style = State()


class TechState(StatesGroup):
    tech = State()
    tech1 = State()
    tech2 = State()
    tech3 = State()
    tech4 = State()
    tech5 = State()
    tech6 = State()
    tech7 = State()


class PriorityState(StatesGroup):
    wish1 = State()
    wish2 = State()


class UserState(StatesGroup):
    name = State()
