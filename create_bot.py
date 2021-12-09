from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
Wallet = {}

TOKEN = '5099923563:AAGy3gM1uR7HD3GoYY-d0SRQp7wITwvqmJw'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


