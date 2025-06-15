from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram import F

from hendlers.state import TechState, PriorityState
from keyboards.keyboard import wish_kb, tech_kb

router = Router()

tech_list2 = dict()


@router.callback_query(F.data == 'cancel')
async def set_end(call, state: FSMContext):
    data = await state.get_data()

    if tech_list2[call.from_user.id] == 'tech':
        tech = data['tech']
        await call.message.edit_text(f'<b>Наполнение кухни</b>:\n{tech}')


    elif tech_list2[call.from_user.id] == 'tech1':
        tech = data['tech']
        tech1 = data['tech1']
        await call.message.edit_text(f'<b>Наполнение кухни</b>:\n{tech},\n{tech1}')

    elif tech_list2[call.from_user.id] == 'tech2':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        await call.message.edit_text(f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2}')

    elif tech_list2[call.from_user.id] == 'tech3':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        await call.message.edit_text(f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                                     f'\n{tech3}')

    elif tech_list2[call.from_user.id] == 'tech4':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        await call.message.edit_text(f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                                     f'\n{tech3},\n{tech4}')

    elif tech_list2[call.from_user.id] == 'tech5':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech5 = data['tech5']
        await call.message.edit_text(f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                                     f'\n{tech3},\n{tech4},\n{tech5}')

    elif tech_list2[call.from_user.id] == 'tech6':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech5 = data['tech5']
        tech6 = data['tech6']
        await call.message.edit_text(f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},\n{tech3}'
                                     f',\n{tech4},\n{tech5},\n{tech6}')

    elif tech_list2[call.from_user.id] == 'tech7':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech5 = data['tech5']
        tech6 = data['tech6']
        tech7 = data['tech7']
        await call.message.edit_text(f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                                     f'\n{tech3},\n{tech4},\n{tech5},'
                                     f'\n{tech6},\n{tech7}')

    await call.message.answer('..............,')
    await call.message.answer('Шаг 5️⃣')
    await call.message.answer('<b>Что для вас приоритетно в заказе?\nВыберите не более 2️⃣ пунктов из списка</b>')

    await call.message.answer('<b>Что для вас наиболее приоритетно</b>: ', reply_markup=wish_kb)
    await call.answer()
    await state.set_state(PriorityState.wish1)


@router.callback_query(F.data == 'reset')
async def set_reset(call, state: FSMContext):
    await call.message.edit_text('Выберите наполнение кухни',
                                 reply_markup=tech_kb)
    await call.answer()
    await state.set_state(TechState.tech)


@router.callback_query(TechState.tech)
async def send_next(call, state: FSMContext):
    await state.update_data(tech=call.data)
    data = await state.get_data()
    tech = data['tech']
    tech_list2[call.from_user.id] = 'tech'

    tech_list = f'<b>Наполнение кухни 1</b>:\n{tech}'

    await call.message.edit_text(tech_list,
                                 reply_markup=tech_kb)
    await call.answer()
    await state.set_state(TechState.tech1)
    return tech_list2


@router.callback_query(TechState.tech1)
async def send_next1(call, state: FSMContext):
    await state.update_data(tech1=call.data)
    data = await state.get_data()
    tech = data['tech']
    tech1 = data['tech1']
    tech_list2[call.from_user.id] = 'tech1'

    tech_list = f'<b>Наполнение кухни 2</b>:\n{tech},\n{tech1}'
    await call.message.edit_text(tech_list,
                                 reply_markup=tech_kb)
    await call.answer()
    await state.set_state(TechState.tech2)
    return tech_list2


@router.callback_query(TechState.tech2)
async def send_next2(call, state: FSMContext):
    await state.update_data(tech2=call.data)
    data = await state.get_data()
    tech = data['tech']
    tech1 = data['tech1']
    tech2 = data['tech2']
    tech_list2[call.from_user.id] = 'tech2'

    tech_list = f'<b>Наполнение кухни 3</b>:\n{tech},\n{tech1},\n{tech2}'
    await call.message.edit_text(tech_list, reply_markup=tech_kb)

    await call.answer()
    await state.set_state(TechState.tech3)
    return tech_list2


@router.callback_query(TechState.tech3)
async def send_next3(call, state: FSMContext):
    await state.update_data(tech3=call.data)
    data = await state.get_data()
    tech = data['tech']
    tech1 = data['tech1']
    tech2 = data['tech2']
    tech3 = data['tech3']
    tech_list2[call.from_user.id] = 'tech3'
    tech_list = f'<b>Наполнение кухни 4</b>:\n{tech},\n{tech1},\n{tech2},\n{tech3}'
    await call.message.edit_text(tech_list,
                                 reply_markup=tech_kb)

    await call.answer()
    await state.set_state(TechState.tech4)


@router.callback_query(TechState.tech4)
async def send_next4(call, state: FSMContext):
    await state.update_data(tech4=call.data)
    data = await state.get_data()
    tech = data['tech']
    tech1 = data['tech1']
    tech2 = data['tech2']
    tech3 = data['tech3']
    tech4 = data['tech4']
    tech_list2[call.from_user.id] = 'tech4'
    tech_list = f'<b>Наполнение кухни 5</b>:\n{tech},\n{tech1},\n{tech2},\n{tech3},\n{tech4}'
    await call.message.edit_text(tech_list, reply_markup=tech_kb)

    await call.answer()
    await state.set_state(TechState.tech5)


@router.callback_query(TechState.tech5)
async def send_next5(call, state: FSMContext):
    await state.update_data(tech5=call.data)
    data = await state.get_data()
    tech = data['tech']
    tech1 = data['tech1']
    tech2 = data['tech2']
    tech3 = data['tech3']
    tech4 = data['tech4']
    tech5 = data['tech5']
    tech_list2[call.from_user.id] = 'tech5'
    tech_list = f'<b>Наполнение кухни 6</b>:\n{tech},\n{tech1},\n{tech2},\n{tech3},\n{tech4}, \n{tech5}'
    await call.message.edit_text(tech_list,
                                 reply_markup=tech_kb)

    await call.answer()
    await state.set_state(TechState.tech6)


@router.callback_query(TechState.tech6)
async def send_next6(call, state: FSMContext):
    await state.update_data(tech6=call.data)
    data = await state.get_data()
    tech = data['tech']
    tech1 = data['tech1']
    tech2 = data['tech2']
    tech3 = data['tech3']
    tech4 = data['tech4']
    tech5 = data['tech5']
    tech6 = data['tech6']
    tech_list2[call.from_user.id] = 'tech6'
    tech_list = (f'<b>Наполнение кухни 7</b>:\n{tech},\n{tech1},\n{tech2},\n{tech3},'
                 f'\n{tech4},\n{tech5},\n{tech6}')
    await call.message.edit_text(tech_list, reply_markup=tech_kb)

    await call.answer()
    await state.set_state(TechState.tech7)


@router.callback_query(TechState.tech7)
async def send_next7(call, state: FSMContext):
    await state.update_data(tech7=call.data)
    data = await state.get_data()

    tech = data['tech']
    tech1 = data['tech1']
    tech2 = data['tech2']
    tech3 = data['tech3']
    tech4 = data['tech4']
    tech5 = data['tech5']
    tech6 = data['tech6']
    tech7 = data['tech7']
    tech_list2[call.from_user.id] = 'tech7'
    tech_list = (f'''
 <b>Наполнение кухни 8</b>:
 {tech},
 {tech1},
 {tech2},
 {tech3}'
 {tech4},
 {tech5},
 {tech6},
 {tech7}
''')
    await call.message.edit_text(tech_list, reply_markup=tech_kb)

    await call.answer()
    await state.set_state(TechState.tech)
