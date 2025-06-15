from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext

from hendlers.state import PriorityState, UserState
from hendlers.tech import tech_list2
from keyboards.keyboard import result_kb, start_kb, wish_kb

router2 = Router()

wish_list = dict()


@router2.callback_query(F.data == 'ok4')
async def send_choice(call: types.CallbackQuery, state: FSMContext):
    global wish, tech_list
    await call.message.edit_text('............')
    await call.answer('Тест завершён 👌 Проверьте результат\n '
                      'и выберите дальнейшее действие.', show_alert=True)
    await call.message.answer('<b>Результат теста</b>')
    data = await state.get_data()
    form = data['form']
    island = data['island']
    style = data['style']
    dlina = data['dlina']
    shirina = data['shirina']
    visota = data['visota']
    potolok = data['potolok']

    if tech_list2[call.from_user.id] == 'tech':
        tech = data['tech']
        tech_list = f'<b>Наполнение кухни</b>:\n{tech}'

    elif tech_list2[call.from_user.id] == 'tech1':
        tech = data['tech']
        tech1 = data['tech1']
        tech_list = f'<b>Наполнение кухни</b>:\n{tech},\n{tech1}'

    elif tech_list2[call.from_user.id] == 'tech2':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech_list = f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2}'

    elif tech_list2[call.from_user.id] == 'tech3':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                     f'\n{tech3}')
    elif tech_list2[call.from_user.id] == 'tech4':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                     f'\n{tech3},\n{tech4}')

    elif tech_list2[call.message.from_user.id] == 'tech5':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech5 = data['tech5']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                     f'\n{tech3},\n{tech4},\n{tech5}')

    elif tech_list2[call.from_user.id] == 'tech6':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech5 = data['tech5']
        tech6 = data['tech6']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},\n{tech3}'
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
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                     f'\n{tech3},\n{tech4},\n{tech5},'
                     f'\n{tech6},\n{tech7}')

    if wish_list[call.from_user.id] == 'wish1':
        wish1 = data['wish1']
        wish = f'<b>В приоритете:</b>\n<i>{wish1}</i>'
    elif wish_list[call.from_user.id] == 'wish2':
        wish1 = data['wish1']
        wish2 = data['wish2']
        wish = f'<b>В приоритете:</b>\n<i>{wish1}</i>\n<i>{wish2}</i>'

    result_list = f'''<b>Форма кухни:</b><i>\n{form}</i>\n
<b>Наличие острова</b>:\n{island}\n
<b>Стиль кухни:</b>\n<i>{style}</i>\n
<b>Размер кухни:</b>\n<i>Длина - {dlina}</i>\n<i>Ширина - {shirina}</i>\n<i>Высота - {visota}</i>\n<i>До потолка - {potolok}</i>\n
{tech_list}\n
{wish}'''
    await call.message.answer(f'{result_list}')
    await call.message.answer(f'Выберите дальнейшеее действие', reply_markup=result_kb)

    await call.answer()


@router2.callback_query(F.data == 'ok5', )
async def send_ok(call, state: FSMContext):
    await call.message.edit_text('<b>Напишите имя по которому к вам можно обращаться: ✏</b>')
    await call.answer()
    await state.set_state(UserState.name)


@router2.callback_query(F.data == 'ok6')
async def send_repeat(call):
    await call.message.edit_text('Нажмите кнопку чтобы начать тестирование', reply_markup=start_kb)
    await call.answer()


@router2.callback_query(PriorityState.wish1)
async def send_wish1(call, state: FSMContext):
    await state.update_data(wish1=call.data)
    wish_list[call.from_user.id] = 'wish1'

    data = await state.get_data()
    wish1 = data['wish1']

    await call.message.edit_text(f'<b>Что для вас наиболее приоритетно</b> - 1:\t\t \n{wish1}',
                                 reply_markup=wish_kb)
    await call.answer()
    if call.data == 'ok5':
        await call.message.edit_text('<b>Напишите имя по которому к вам можно обращаться</b>')
        await state.set_state(UserState.name)
    else:
        await state.set_state(PriorityState.wish2)


@router2.callback_query(PriorityState.wish2)
async def send_wish2(call, state: FSMContext):
    await state.update_data(wish2=call.data)
    wish_list[call.from_user.id] = 'wish2'
    data = await state.get_data()
    wish1 = data['wish1']
    wish2 = data['wish2']

    await call.message.edit_text(f'<b>Что для вас наиболее приоритетно</b> - 2:\t\t\n{wish1},\n{wish2}',
                                 reply_markup=wish_kb)
    await call.answer()
    await state.set_state(PriorityState.wish1)
