from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


###############################################
'''######### Старотавая клавиатура ##########'''

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/start')]], resize_keyboard=True, one_time_keyboard=True)

################################################
''' Клавиатура запускающая тестирование'''

start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пройти тест 📝', callback_data='test')]])

################################################
""" Клавиатура в блоке размеров с потверждением предела высоты кухни """

yes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да ✅', callback_data='Да'),
     InlineKeyboardButton(text='Нет ❌', callback_data='Нет')]])

################################################
""" Клавиатура в конце тестирования """

result_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подтвердить результат\t\t✅', callback_data='ok5')],
    [InlineKeyboardButton(text='Пройти тест заново\t\t🔁', callback_data='ok6')]])

################################################

""" Клавиатура текстовая, с выбором формы кухни """

forms_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Прямая')],
    [KeyboardButton(text='Г-образная')],
    [KeyboardButton(text='П-образная')], ], resize_keyboard=True, one_time_keyboard=True,
    input_field_placeholder='Выберите форму вашей кухни')

################################################
""" Клавиатура текстовая, с выбором стиля кухни"""
style_kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Классика '),
         KeyboardButton(text='Хайтек , ручка гола')],
        [KeyboardButton(text='Неоклассика '),
         KeyboardButton(text='Современный стиль ')],
        [KeyboardButton(text='Есть дизайн проект ')],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите стиль кухни')

################################################
''' Клавиатура с выбором кухонной техники'''

tech_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посудомойка 🫧', callback_data='Посудомойка '),
     InlineKeyboardButton(text='Духовой шкаф 🥧', callback_data='Духовой шкаф')],
    [InlineKeyboardButton(text='Холодильник встроенный ❄', callback_data='Холодильник встроенный '),
     InlineKeyboardButton(text='Холодильник 🧊', callback_data='Холодильник')],
    [InlineKeyboardButton(text='Подсветка 💡', callback_data='Подсветка '),
     InlineKeyboardButton(text='Стиральная машина 🥼', callback_data='Стиральная машина')],
    [InlineKeyboardButton(text='Витринные шкафы 🪟', callback_data='Витринные шкафы '),
     InlineKeyboardButton(text='Встраиваемая микроволновка 🍿', callback_data='Встраиваемая микроволновка')],
    [InlineKeyboardButton(text="Выбрать ✅", callback_data="cancel")],
    [InlineKeyboardButton(text="Сбросить 🗑", callback_data="reset")], ])


################################################
''' Кавиатура в конце блока размера кухни'''

back3_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Далее ⏭")],
    [KeyboardButton(text="Ввести заново ⏮")], ], resize_keyboard=True, one_time_keyboard=True)


################################################
''' Клавиатра в блоке priority '''

wish_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сроки ⏳', callback_data='Сроки')],
        [InlineKeyboardButton(text='Внешний вид 🎨', callback_data='Внешний вид')],
        [InlineKeyboardButton(text='Качество 🏆', callback_data='Качество')],
        [InlineKeyboardButton(text='Цена 💵', callback_data='Цена')],
        [InlineKeyboardButton(text='Далее ✅', callback_data='ok4')]])
