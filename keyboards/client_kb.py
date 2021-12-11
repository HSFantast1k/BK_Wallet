from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

"""
Кнопки клавиатуры клиента
"""

button_1 = KeyboardButton('Баланс Wallet 👛')
button_2 = KeyboardButton('Все транзакции 🔁')
button_3 = KeyboardButton('Частичные транзакции 🔎')
button_4 = KeyboardButton('Доступные команды 👋')
button_5 = KeyboardButton('О боте 🤖')

"""
Инлайн клавиатура выбора категории
"""

category_button_1 = KeyboardButton('Продукты 🥦')
category_button_2 = KeyboardButton('Транспорт 🚀')
category_button_3 = KeyboardButton('Дом 🏠')
category_button_4 = KeyboardButton('Развлечения 🎡')
category_button_5 = KeyboardButton('Online Profit 🤑')
category_button_6 = KeyboardButton('Бьюти 💄')
category_button_7 = KeyboardButton('Другие ➡️')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

inline_kb_client = ReplyKeyboardMarkup().row(category_button_1, category_button_2).row(
    category_button_3, category_button_4).row(category_button_5, category_button_6).row(category_button_7)


kb_client.add(button_1).row(button_2, button_3).row(button_4, button_5)
