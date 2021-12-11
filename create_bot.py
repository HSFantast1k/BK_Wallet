from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '5099923563:AAGy3gM1uR7HD3GoYY-d0SRQp7wITwvqmJw'
ADMIN_ID = '1320695651', '2120097260'  # 2120097260 - @work_BK_account, 1320695651 - @iamBohdan
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
