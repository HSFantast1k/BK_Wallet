from aiogram.utils import executor
from create_bot import dp

from handlers import client
from handlers import admin
from handlers import other

client.registe_handlers_client(dp)
# admin.registe_handlers_client(dp)
other.registe_handlers_client(dp)


async def on_startup(_):
    print('Бот вышел в онлайн')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
