from aiogram import Dispatcher, types
from config import Admins
from keyboards import buttons

async def start(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer('🚀 О Нас: '
                             '\n\n'
                             'Привет! 🙌🏼\n'
                             'Я — бот Kulaktandyruu, Я надежный помощник в мире эффективной рекламы в Telegram. '
                             'Я создан, чтобы упростить процесс продвижения ваших продуктов и услуг.'
                             '\n\n'
                             '💳 Платежи:\n'
                             'У меня простая система оплаты. Внесите средства по реквизитам и всё, ваша реклама будет готова!'
                             '\n\n'
                             '🤖 Техподдержка:\n'
                             'Наши специалисты готовы помочь вам в любое время. Если у вас возникли вопросы или проблемы, '
                             'обратитесь к нашей техподдержке.'
                             '\n\n'
                             '🌐 Интеграция:\n'
                             'Размещайте рекламу не только в Telegram, но и в других соц.сетях! 📢',
                             reply_markup=buttons.StartForAdmin)

    else:
        await message.answer('🚀 О Нас: '
                             '\n\n'
                             'Привет! 🙌🏼\n'
                             'Я — бот Kulaktandyruu, Я надежный помощник в мире эффективной рекламы в Telegram. '
                             'Я создан, чтобы упростить процесс продвижения ваших продуктов и услуг.'
                             '\n\n'
                             '💳 Платежи:\n'
                             'У меня простая система оплаты. Внесите средства по реквизитам и всё, ваша реклама будет готова!'
                             '\n\n'
                             '🤖 Техподдержка:\n'
                             'Наши специалисты готовы помочь вам в любое время. Если у вас возникли вопросы или проблемы, '
                             'обратитесь к нашей техподдержке.'
                             '\n\n'
                             '🌐 Интеграция:\n'
                             'Размещайте рекламу не только в Telegram, но и в других соц.сетях! 📢',
                             reply_markup=buttons.OrderForStart)

async def support(message: types.Message):
    await message.answer('Наша тех.поддержка:\n'
                         '@kulaktandyruu_Bishkek', reply_markup=buttons.Start)

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(support, commands=['support'])
