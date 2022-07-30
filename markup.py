from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Main Menu ---#
btnTon = KeyboardButton('Top Charts')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTon)

