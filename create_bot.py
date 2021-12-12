from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '5099923563:AAGy3gM1uR7HD3GoYY-d0SRQp7wITwvqmJw'  # 5025608224:AAEfFkMMT_8qyjszF62imqmeVU3iepfhFnI -TEST
ADMIN_ID = [1320695651, 2120097260]  # 2120097260 - @work_BK_account, 1320695651 - @iamBohdan
USERS_CHAT_ID = {}
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
