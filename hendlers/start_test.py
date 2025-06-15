from hendlers.name import admin, router_start
from hendlers.state import TasteState, SizeState

from keyboards.keyboard import start_kb, forms_kb, kb,style_kb

from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram import types
from aiogram.fsm.context import FSMContext

import time


async def start_message(message: types.Message):
    # await message.answer_sticker('CAACAgIAAxkBAAIOJGgom2fW8FfZDFoaP6TzazTsBREXAAJuBQACP5XMCoY62V2IvLc1NgQ')
    await message.answer(
        f'🖐Здравствуйте <b>{message.from_user.full_name}</b>!\n\n Вас приветствует\n <b>Бот ВорошиловМебель !</b>\n\n'
        'Чтобы мы могли лучше понять ваш запрос\n пройдите пожалуйста небольшой тест,\n'
        'состоящий из 5 вопросов'
    )
    await message.answer('********************************'
                         '', time.sleep(1),reply_markup=ReplyKeyboardRemove())
    await message.answer('<b>Нажмите кнопку чтобы начать тестирование</b>', reply_markup=start_kb)
    await message.bot.send_message(chat_id=admin, text=f"Ваш ID: {message.from_user.id}")


async def test_start(call, state: FSMContext):
    await call.message.answer('Шаг 1⃣',reply_markup=ReplyKeyboardRemove())
    await call.message.answer('<b>Выберите форму вашей кухни</b>')
    time.sleep(1)
    photo = FSInputFile('files/form.jpeg')
    await call.message.answer_photo(photo=photo, caption='<b>Прямая</b>')
    photo = FSInputFile('files/form2.jpg', )
    await call.message.answer_photo(photo=photo, caption='<b>Г-образная</b>')
    photo = FSInputFile('files/form3.jpg')
    await call.message.answer_photo(photo=photo, caption='<b>П-образная</b>')
    await call.message.answer('<b>Выберите форму вашей кухни</b>', reply_markup=forms_kb)
    await call.answer()

    await state.set_state(TasteState.form)


async def set_island(message, state: FSMContext):
    await state.update_data(form=message.text)
    photo = FSInputFile('files/form4.jpg')
    island_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Да✅', callback_data='Да'),
             InlineKeyboardButton(text='Нет❌', callback_data='Нет')]
        ],
    )
    await message.answer_photo(photo=photo, caption='<b>Наличие острова: да/нет</b>', reply_markup=island_kb)

    await state.set_state(TasteState.island)


async def send_forward2(call, state: FSMContext):
    await state.update_data(island=call.data)
    await call.message.reply("Шаг 2⃣", reply_markup=ReplyKeyboardRemove())
    await call.message.answer('<b>Выберите стиль вашей кухни</b>')

    photo1 = FSInputFile('files/classic.jpg')
    await call.message.answer_photo(photo=photo1, caption='<b>Классика</b>', )

    photo = FSInputFile('files/hitech.jpg')
    await call.message.answer_photo(photo=photo, caption='<b>Хайтек, ручка гола</b>')

    photo = FSInputFile('files/neoclassic.jpg')
    await call.message.answer_photo(photo=photo, caption="<b>Неоклассика</b>")

    photo = FSInputFile('files/provans.jpg')
    await call.message.answer_photo(photo=photo, caption="<b>Современный стиль</b>")
    await call.message.answer('<b>Выберите стиль вашей кухни</b>', reply_markup=style_kb)
    await call.answer()
    await state.set_state(TasteState.style)


async def send_forward3(message, state: FSMContext):
    await state.update_data(style=message.text)
    await message.reply("Шаг 3⃣", reply_markup=ReplyKeyboardRemove())
    await message.answer('Введите размеры  вашей кухни 📏', time.sleep(1))
    await message.answer('<b>Введите длину кухни: </b> ✏')
    await state.set_state(SizeState.dlina)


@router_start.message()
async def start(message):
    await message.answer('Нажмите <b>/start</b> чтобы начать общение', reply_markup=kb)
