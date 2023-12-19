from aiogram.utils import executor
import logging
from db.ORM import sql_create

# ===========================================================================
from config import dp, bot, Admins
from handlers import commands, fsm_advertising, get_advertising


# ==================================================================================================================
async def on_startup(_):
    for Admin in Admins:
        await bot.send_message(chat_id=Admin, text="Бот запущен!", reply_markup=None)
        await sql_create()

commands.register_commands(dp)
fsm_advertising.register_advertising(dp)
get_advertising.sql_get(dp)

# ===========================================================================
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
