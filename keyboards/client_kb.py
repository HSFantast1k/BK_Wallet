from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

"""
Кнопки клавиатуры клиента
"""

button_1 = KeyboardButton('Посмотреть доступные команды 👋')
button_2 = KeyboardButton('Баланс Wallet 👛')
button_3 = KeyboardButton('Посмотреть все расходы 💰')
button_4 = KeyboardButton('О создателе 👨‍💻')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button_2).add(button_3).row(button_1, button_4)
