import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from app.keyboards import kb, kb_add, kb_admin, catalog_list

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    sticker_id = os.getenv('STICKER_ID')
    await message.answer_sticker(sticker_id)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'You are logged in as an administrator', reply_markup=kb_add)
    else:
        await message.answer(f'Hello {message.from_user.full_name}', reply_markup=kb)


@dp.message()
async def buttons_click(message: Message):
    if message.text == 'Catalogue':
        await message.answer(f'Here is our Catalogue', reply_markup=catalog_list)
    elif message.text == 'Card':
        await message.answer(f'Added to card')
    elif message.text == 'Contacts':
        await message.answer(f'Buy here: @no_user')
    elif message.from_user.id == int(os.getenv('ADMIN_ID')) and message.text == 'Admin keyboard':
        await message.answer(f'You have opened the admin keyboard', reply_markup=kb_admin)
    elif message.text == 'id':
        await message.answer(f'{message.from_user.id}')
    else:
        await message.reply(f'Don\'t understand you')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(dp.start_polling(bot))
