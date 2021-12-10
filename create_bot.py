from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '123456:QWERTY'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
