import sqlite3
from db import sql_queris

db = sqlite3.connect("db/all_advertising")
cursor = db.cursor()


async def sql_create():
    if db:
        print("База Бишкек подключена!")
    cursor.execute(sql_queris.CREATE_TABLE_ADVERTISING)
    db.commit()


async def sql_insert_advertising(state):
    async with state.proxy() as data:
        cursor.execute(sql_queris.INSERT_INTO_TABLE_ADVERTISING, (
            data.get('tariff'),
            data.get('photo_check'),
            data.get('user_name'),
            data.get('user_id'),
            data.get('info'),
            data.get('info_photo', None),
            data.get('social_network')
        ))

        db.commit()
