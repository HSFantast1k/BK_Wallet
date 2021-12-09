from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

from handlers import client
from handlers import admin
from handlers import other


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()


client.registe_handlers_client(dp)
# admin.registe_handlers_client(dp)
other.registe_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
