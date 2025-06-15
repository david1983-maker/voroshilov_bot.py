from aiogram import Bot, Dispatcher, F
import asyncio
import os
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters.command import Command

import logging

from hendlers.admin import set_admin
from hendlers.name import send_name

from hendlers.priority import router2
from hendlers.tech import router
from hendlers.size import *
from hendlers.start_test import *
from hendlers.state import TasteState, SizeState, UserState

from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

dp.message.register(start_message, F.text, Command('start'))
dp.message.register(set_admin, F.text, Command('admin'))
dp.message.register(send_name, UserState.name)

dp.callback_query.register(test_start, F.data == 'test')

dp.callback_query.register(send_forward2, TasteState.island)
dp.message.register(set_island, TasteState.form)
dp.message.register(send_forward3, TasteState.style)
dp.message.register(set_shirina, SizeState.dlina)
dp.message.register(set_visota, SizeState.shirina)
dp.message.register(set_potolok, SizeState.visota)
dp.callback_query.register(set_fin, SizeState.potolok)
dp.message.register(send_choice, F.text.contains("Далее ⏭"))
dp.message.register(set_size, F.text.contains("Ввести заново ⏮"))


async def main():
    dp.include_router(router)
    dp.include_router(router2)
    dp.include_router(router_start)
    try:
        logging.basicConfig(level=logging.INFO)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, scip_update=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
