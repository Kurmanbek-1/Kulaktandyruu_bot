from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

TOKEN = config('TOKEN')

Admins = [6424789388, 995712956, ]

bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)
