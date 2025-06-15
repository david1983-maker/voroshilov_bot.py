import os

from aiogram import Router
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from hendlers.tech import tech_list2
from hendlers.priority import wish_list




load_dotenv()
admin = int(os.getenv('ADMIN_ID'))


async def send_name(message, state: FSMContext):
    global tech_list, wish
    await state.update_data(name=message.text)
    data = await state.get_data()
    form = data['form']
    island = data['island']
    style = data['style']
    dlina = data['dlina']
    shirina = data['shirina']
    visota = data['visota']
    potolok = data['potolok']

    name = data['name']

    if tech_list2[message.from_user.id] == 'tech':
        tech = data['tech']
        tech_list = f'<b>Наполнение кухни</b>:\n{tech}'

    elif tech_list2[message.from_user.id] == 'tech1':
        tech = data['tech']
        tech1 = data['tech1']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1}')

    elif tech_list2[message.from_user.id] == 'tech2':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2}')

    elif tech_list2[message.from_user.id] == 'tech3':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                     f'\n{tech3}')

    elif tech_list2[message.from_user.id] == 'tech4':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech_list = f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},\n{tech3},\n{tech4}'

    elif tech_list2[message.from_user.id] == 'tech5':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech5 = data['tech5']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},'
                     f'\n{tech3},\n{tech4},\n{tech5}')

    elif tech_list2[message.from_user.id] == 'tech6':
        tech = data['tech']
        tech1 = data['tech1']
        tech2 = data['tech2']
        tech3 = data['tech3']
        tech4 = data['tech4']
        tech5 = data['tech5']
        tech6 = data['tech6']
        tech_list = (f'<b>Наполнение кухни</b>:\n{tech},\n{tech1},\n{tech2},\n{tech3}'
                     f',\n{tech4},\n{tech5},\n{tech6}')

    elif tech_list2[message.from_user.id] == 'tech7':
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

    if wish_list[message.from_user.id] == 'wish1':
        wish1 = data['wish1']
        wish = f'<b>В приоритете:</b>\n<i>{wish1}</i>'
    elif wish_list[message.from_user.id] == 'wish2':
        wish1 = data['wish1']
        wish2 = data['wish2']
        wish = f'<b>В приоритете:</b>\n<i>{wish1}</i>\n<i>{wish2}</i>'

    result_list = f'''<b>Форма кухни:</b><i>\n{form}</i>\n
<b>Наличие острова</b>:\n<i>{island}</i>\n
<b>Стиль кухни:</b>\n<i>{style}</i>\n
<b>Размер кухни:</b>\n<i>Длина - {dlina}</i>\n<i>Ширина - {shirina}</i>\n<i>Высота - {visota}</i>\n<i>До потолка - {potolok}</i>\n
{tech_list}\n
{wish}\n
<b>Заказчик:</b>\n<b><i>{name}</i></b>
'''
    await message.answer('✉ Результат опроса отправлен администратору 📬')

    await message.answer('Спасибо за участие в тесте 🤝!.\nВ ближайшее время с вами свяжутся ☎')
    await message.bot.send_message(chat_id=admin, text=result_list)
    await message.bot.send_message(chat_id=-1002594736827, text=result_list)

    await state.clear()


router_start = Router()
