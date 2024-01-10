import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart, Filter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from app import database as db
from app import keyboards as kb

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
router = Router()


class CommandFilter(Filter):
    def __init__(self, command: str) -> None:
        self.command = command

    async def __call__(self, message: Message) -> bool:
        text = message.text.split()
        command = f'/{text[0].lower()}'
        return len(text) > 0 and command == f'{self.command}'


@router.message(CommandFilter("/card"))
async def card(message: Message) -> None:
    await message.answer('Added to card')


@router.message(CommandFilter("/catalogue"))
async def catalogue(message: Message) -> None:
    await message.answer(f'Here is our Catalogue', reply_markup=kb.catalog_list)


@router.message(CommandFilter("/contacts"))
async def contacts(message: Message) -> None:
    await message.answer(f'Buy here: @no_user')


async def on_startup():
    await db.db_start()
    print('DB connected')


class NewOrder(StatesGroup):
    type = State()
    name = State()
    desc = State()
    price = State()
    photo = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await db.cmd_start_db(message.from_user.id)
    sticker_id = os.getenv('STICKER_ID')
    await message.answer_sticker(sticker_id)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'You are logged in as an administrator', reply_markup=kb.kb_add)
    else:
        await message.answer(f'Hello {message.from_user.full_name}', reply_markup=kb.kb_user)


# @dp.message()
# async def buttons_click(message: Message):
#     elif message.from_user.id == int(os.getenv('ADMIN_ID')) and message.text == 'Admin keyboard':
#         await message.answer(f'You have opened the admin keyboard', reply_markup=kb.kb_admin)
#     elif message.text == 'id':
#         await message.answer(f'{message.from_user.id}')
#     elif message.text == 'Add goods':
#         await NewOrder.type.set()
#         await message.answer(f'Choose type', reply_markup=kb.catalog_list)
#     else:
#         await message.reply(f'Don\'t understand you')


# @dp.callback_query(state=NewOrder.type)
# async def add_item_type():
#     pass


@dp.callback_query()
async def callback_query_keyboard(callback_query: CallbackQuery):
    if callback_query.data == 't-shirt':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You choose t-shirts')
    elif callback_query.data == 'shorts':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You choose shorts')
    elif callback_query.data == 'sneakers':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You choose sneakers')


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
