import time

from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from hendlers.state import SizeState, TechState
from keyboards.keyboard import yes_kb, back3_kb, tech_kb
from aiogram.fsm.context import FSMContext


async def set_shirina(message, state: FSMContext):
    await state.update_data(dlina=message.text)
    await message.answer('<b>Введите ширину кухни: </b>✏')
    await state.set_state(SizeState.shirina)


async def set_visota(message, state: FSMContext):
    await state.update_data(shirina=message.text)
    await message.answer('<b>Введите высоту кухни: </b>✏')
    await state.set_state(SizeState.visota)


async def set_potolok(message, state: FSMContext):
    await state.update_data(visota=message.text)
    await message.answer('До потолка: <b>да/нет?</b>', reply_markup=yes_kb)
    await state.set_state(SizeState.potolok)


async def set_fin(callback: CallbackQuery, state: FSMContext):
    await state.update_data(potolok=callback.data)
    data = await state.get_data()

    d = data['dlina']
    sh = data['shirina']
    v = data['visota']
    p = data['potolok']
    ans = (
           f'<b>Размер кухни</b>: \n'
           f'<i>Длина</i> - {d}\n'
           f'<i>Ширина</i> - {sh}\n'
           f'<i>Высота</i> - {v}\n'
           f'<i>До потолка</i>- {p}\n'

           f'...........\n')

    await callback.message.answer(ans, reply_markup=back3_kb)
    await callback.answer()


async def send_choice(message, state: FSMContext):
    await message.answer('Шаг 4⃣')
    await message.reply('<b>Выберите наполнение которое  вы хотите видеть в вашей кухне</b>',
                        reply_markup=ReplyKeyboardRemove())

    await message.answer('Выберите наполнение кухни', time.sleep(1),
                         reply_markup=tech_kb)

    await state.set_state(TechState.tech)


async def set_size(message, state: FSMContext):
    await message.reply('<b>Введите длину кухни</b> ↔️', reply_markup=ReplyKeyboardRemove())

    await state.set_state(SizeState.dlina)
