from aiogram.utils import executor
import logging

# ===========================================================================
from config import dp, bot, Admins
from handlers import commands, fsm_advertising


# ==================================================================================================================
async def on_startup(_):
    for Admin in Admins:
        await bot.send_message(chat_id=Admin, text="Бот запущен!", reply_markup=None)

commands.register_commands(dp)
fsm_advertising.register_advertising(dp)

# ===========================================================================
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
