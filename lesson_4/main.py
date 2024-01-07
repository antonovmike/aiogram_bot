import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

button_1 = KeyboardButton(text='Catalogue')
button_2 = KeyboardButton(text='Card')
button_3 = KeyboardButton(text='Contacts')
raw_1 = [button_1, button_2]
raw_2 = [button_3]
kb = ReplyKeyboardMarkup(keyboard=[raw_1, raw_2], resize_keyboard=True)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    sticker_id = 'CAACAgIAAxkBAAIUSWWalI3UK4cUW2s25m49M2WlW6SZAAI7AQACijc4AAGSEIzViMEnBDQE'
    await message.answer_sticker(sticker_id)
    await message.answer(f'Hello {message.from_user.full_name}', reply_markup=kb)


@dp.message()
async def buttons_click(message: Message):
    if message.text == 'Catalogue':
        await message.answer(f'Here is our Catalogue')
    elif message.text == 'Card':
        await message.answer(f'Added to card')
    elif message.text == 'Contacts':
        await message.answer(f'Buy here: @no_user')


@dp.message()
async def forward_message(message: Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)


@dp.message()
async def answer(message: Message) -> None:
    await message.reply(f'Don\'t understand you')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(dp.start_polling(bot))
