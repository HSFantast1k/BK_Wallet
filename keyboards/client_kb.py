from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

"""
Кнопки клавиатуры клиента
"""

button_1 = KeyboardButton('Посмотреть доступные команды 👋')
button_2 = KeyboardButton('Баланс Wallet 👛')
button_3 = KeyboardButton('Посмотреть все транзакции 🔁')
button_4 = KeyboardButton('О создателе и будущих обновлений 👨‍💻')

"""
Инлайн клавиатура выбора категории
"""

inline_button_1 = KeyboardButton('Продукты 🥦')
inline_button_2 = KeyboardButton('Транспорт 🚀')
inline_button_3 = KeyboardButton('Дом 🏠')
inline_button_4 = KeyboardButton('Развлечения 🎡')
inline_button_5 = KeyboardButton('Online Profit 🤑')
inline_button_6 = KeyboardButton('Бьюти 💄')
inline_button_7 = KeyboardButton('Другие ➡️')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

inline_kb_client = ReplyKeyboardMarkup().row(inline_button_1, inline_button_2).row(
    inline_button_3, inline_button_4).row(inline_button_5, inline_button_6).row(inline_button_7)

# kb_client.add(button_2).add(button_3).row(button_1, button_4)
# kb_client.row(button_2, button_3).row(button_1, button_4)
kb_client.add(button_2).add(button_3).add(button_1).add(button_4)
