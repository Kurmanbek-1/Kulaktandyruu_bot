from aiogram import Dispatcher, types
from config import Admins
from keyboards.buttons import StartForAdmin


async def start(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer('🚀 О Нас: '
                             '\n\n'
                             'Привет! 🙌🏼\n'
                             'Мы — бот Kulaktandyruu, ваш надежный помощник в мире эффективной рекламы в Telegram. '
                             'Мы созданы, чтобы упростить процесс продвижения ваших продуктов и услуг.'
                             '\n\n'
                             '💳 Платежи:\n'
                             'У нас простая система оплаты. Внесите средства по реквизитам и всё, ваша реклама будет готова!'
                             '\n\n'
                             '🤖 Техподдержка:\n'
                             'Наши специалисты готовы помочь вам в любое время. Если у вас возникли вопросы или проблемы, '
                             'обратитесь к нашей техподдержке.'
                             '\n\n'
                             '🌐 Интеграция:\n'
                             'Размещайте рекламу не только в Telegram! 📢', reply_markup=StartForAdmin)

    else:
        await message.answer('🚀 О Нас: '
                             '\n\n'
                             'Привет! 🙌🏼\n'
                             'Мы — бот Kulaktandyruu, ваш надежный помощник в мире эффективной рекламы в Telegram. '
                             'Мы созданы, чтобы упростить процесс продвижения ваших продуктов и услуг.'
                             '\n\n'
                             '💳 Платежи:\n'
                             'У нас простая система оплаты. Внесите средства по реквизитам и всё, ваша реклама будет готова!'
                             '\n\n'
                             '🤖 Техподдержка:\n'
                             'Наши специалисты готовы помочь вам в любое время. Если у вас возникли вопросы или проблемы, '
                             'обратитесь к нашей техподдержке.'
                             '\n\n'
                             '🌐 Интеграция:\n'
                             'Размещайте рекламу не только в Telegram! 📢', reply_markup=None)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
