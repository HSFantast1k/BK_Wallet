from aiogram import types, Dispatcher
from create_bot import dp, bot, ADMIN_ID
from data_base import sqlite_db


@dp.message_handler(lambda message: message.text.startswith('check'))
async def admin_check(message: types.Message):
    if str(message.from_user.id) in ADMIN_ID:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.send_message(chat_id=message.chat.id, text='Хорошо хозяин 🤓')
        await sqlite_db.sql_read(message, user_id=int(message.text.split(" ")[1]))
    else:
        await bot.send_message(chat_id=message.chat.id, text='Нет такой команды')
