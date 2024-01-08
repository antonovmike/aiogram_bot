import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

button_1 = KeyboardButton(text='Catalogue')
button_2 = KeyboardButton(text='Card')
button_3 = KeyboardButton(text='Contacts')
button_4 = KeyboardButton(text='Admin keyboard')
raw_1 = [button_1, button_2, button_3]
raw_2 = [button_4]
kb = ReplyKeyboardMarkup(keyboard=[raw_1], resize_keyboard=True)
kb_add = ReplyKeyboardMarkup(keyboard=[raw_1, raw_2], resize_keyboard=True)
button_5 = KeyboardButton(text='Add goods')
button_6 = KeyboardButton(text='Delete goods')
button_7 = KeyboardButton(text='Mail campaign')
raw_1 = [button_5, button_6, button_7]
kb_admin = ReplyKeyboardMarkup(keyboard=[raw_1], resize_keyboard=True)


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
        await message.answer(f'Here is our Catalogue')
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
