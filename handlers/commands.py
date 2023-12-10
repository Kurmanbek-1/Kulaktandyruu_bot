from aiogram import Dispatcher, types

async def start(message: types.Message):
    await message.answer('Добро пожаловать в рекламный бот "Kulaktandyruu 📢"!')


async def info(message: types.Message):
    await message.answer('')


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['info'])