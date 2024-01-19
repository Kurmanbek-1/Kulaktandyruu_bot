from aiogram import types, Dispatcher
import os
from config import bot
from db.ORM import cursor
from db import sql_queris


async def get_advertising(message: types.Message):
    advertisings = cursor.execute(sql_queris.SELECT_CHECKS_ALL).fetchall()

    for advertising in advertisings:
        if advertising[6]:
            await message.answer_photo(photo=advertising[2], caption=f'Информация: {advertising[5]}\n'
                                                                     f'User_ID: {advertising[3]}\n'
                                                                     f'Username: {advertising[4]}\n'
                                                                     f'Тариф: {advertising[1]}\n'
                                                                     f'Где нужно прорекламировать: {advertising[7]}',
                                       reply_markup=None)
            await bot.send_photo(chat_id=message.from_user.id, photo=advertising[6])

        else:
            await message.answer_photo(photo=advertising[2], caption=f'Информация: {advertising[5]}\n'
                                                                     f'User_ID: {advertising[3]}\n'
                                                                     f'Username: {advertising[4]}\n'
                                                                     f'Тариф: {advertising[1]}\n'
                                                                     f'Где нужно прорекламировать: {advertising[7]}',
                                       reply_markup=None)


def sql_get(dp: Dispatcher):
    dp.register_message_handler(get_advertising, commands=['all_advertising', "Все_заказанные!"])
