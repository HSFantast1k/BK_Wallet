from aiogram import types, Dispatcher
from create_bot import bot, dp

"""
@dp.message_handler()
"""


async def other(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(chat_id=message.chat.id, text="Нет такой команды")


def registe_handlers_client(dp: Dispatcher):
    dp.register_message_handler(other)
