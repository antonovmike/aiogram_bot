import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer_sticker('CAACAgIAAxkBAAIUSWWalI3UK4cUW2s25m49M2WlW6SZAAI7AQACijc4AAGSEIzViMEnBDQE')
    await message.answer(f'Hello {message.from_user.full_name}')


@dp.message()
async def check_sticker(message: types.Sticker):
    sticker_id = message.sticker.file_id
    group_id = message.chat.id
    await message.reply(sticker_id)
    await bot.send_message(message.from_user.id, str(group_id))


@dp.message()
async def answer(message: types.Message) -> None:
    await message.reply(f'Don\'t understand you')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(dp.start_polling(bot))
