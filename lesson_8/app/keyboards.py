from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


button_1 = KeyboardButton(text='Catalogue')
button_2 = KeyboardButton(text='Card')
button_3 = KeyboardButton(text='Contacts')
button_4 = KeyboardButton(text='Admin keyboard')
raw_1 = [button_1, button_2, button_3]
raw_2 = [button_4]

kb_user = ReplyKeyboardMarkup(keyboard=[raw_1], resize_keyboard=True)
kb_add = ReplyKeyboardMarkup(keyboard=[raw_1, raw_2], resize_keyboard=True)

button_5 = KeyboardButton(text='Add goods')
button_6 = KeyboardButton(text='Delete goods')
button_7 = KeyboardButton(text='Mail campaign')
raw_3 = [button_5, button_6, button_7]

kb_admin = ReplyKeyboardMarkup(keyboard=[raw_3], resize_keyboard=True)

inline_button_1 = InlineKeyboardButton(text='Shirts', callback_data='t-shirt')
inline_button_2 = InlineKeyboardButton(text='T-Shirts', callback_data='shorts')
inline_button_3 = InlineKeyboardButton(text='Sneakers', callback_data='sneakers')
inline_raw_1 = [inline_button_1, inline_button_2]
inline_raw_2 = [inline_button_3]

catalog_list = InlineKeyboardMarkup(inline_keyboard=[inline_raw_1, inline_raw_2])

button_5 = KeyboardButton(text='Cancel')
raw_4 = [button_5]
cancel = ReplyKeyboardMarkup(keyboard=[raw_4], resize_keyboard=True)
