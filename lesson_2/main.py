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
    await message.answer(f'Hello {message.from_user.full_name}')


@dp.message()
async def answer(message: types.Message) -> None:
    await message.reply(f'Don\'t understand you')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(dp.start_polling(bot))
