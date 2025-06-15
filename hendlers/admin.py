import time
from aiogram import types

from hendlers.name import admin
from dotenv import load_dotenv

load_dotenv()


async def set_admin(message: types.Message):
    if message.from_user.id == admin:
        await message.answer('Добро пожаловать в админ панель', time.sleep(1))

        # await message.answer(f"Ваш ID: {message.from_user.id}")

    else:
        await message.answer('Доступ закрыт')
