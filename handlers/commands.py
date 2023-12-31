from aiogram import Dispatcher, types
from config import Admins
from keyboards import buttons


async def start(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer('🚀 О Нас: '
                             '\n\n'
                             'Приветствую тебя👋\n'
                             'Я — бот Kulaktandyruu,\n'
                             'Я надежный помощник в мире эффективной рекламы в Telegram. Я создан, '
                             'чтобы упростить процесс продвижения ваших продуктов и услуг.'
                             '\n\n'
                             '💳 Платежи:\n'
                             'У меня простая система оплаты. Внесите средства по реквизитам и всё, ваша реклама будет готова!'
                             '\n\n'
                             '🤖 Техподдержка:\n'
                             'Наши специалисты готовы помочь вам в любое время. Если у вас возникли вопросы или проблемы, обратитесь к нашей техподдержке.'
                             '\n\n'
                             '📌Внимание!\n'
                             'Обязательно прочтите правила перед использованием бота!',
                             reply_markup=buttons.StartForAdmin)

    else:
        await message.answer('🚀 О Нас: '
                             '\n\n'
                             'Приветствую тебя👋\n'
                             'Я — бот Kulaktandyruu,\n'
                             'Я надежный помощник в мире эффективной рекламы в Telegram. Я создан, '
                             'чтобы упростить процесс продвижения ваших продуктов и услуг.'
                             '\n\n'
                             '💳 Платежи:\n'
                             'У меня простая система оплаты. Внесите средства по реквизитам и всё, ваша реклама будет готова!'
                             '\n\n'
                             '🤖 Техподдержка:\n'
                             'Наши специалисты готовы помочь вам в любое время. Если у вас возникли вопросы или проблемы, обратитесь к нашей техподдержке.'
                             '\n\n'
                             '📌Внимание!\n'
                             'Обязательно прочтите правила перед использованием бота!',
                             reply_markup=buttons.OrderForStart)


async def support(message: types.Message):
    await message.answer('Наша тех.поддержка:\n'
                         '@kulaktandyruu_Bishkek', reply_markup=buttons.Start)


async def rule(message: types.Message):
    await message.answer("📌ПРАВИЛА\n\n"
                         "Добро пожаловать!\n"
                         "Прежде чем начать взаимодействие с ботом, пожалуйста, прочитайте наши правила. "
                         "Это поможет вам лучше понять, как использовать бот и избежать возможных недоразумений."
                         "\n\n"
                         "⚠️ Важно:\n"
                         "Нарушение правил может повлечь за собой ограничения в использовании бота."
                         "\n\n"
                         "🛑Вакансия должна содержать четкую информацию о требованиях к кандидатам и их обязанностях. "
                         "Это поможет кандидатам лучше понять, подходит ли им данная вакансия."
                         "\n\n"
                         "🛑Автор вакансии несет ответственность за предоставленную информацию. Администрация бота не "
                         "несет ответственности за условия трудоустройства или действия компании. "
                         "\n\n"
                         "🛑Все размещаемые вакансии должны соответствовать действующим законам в области трудоустройства. "
                         "Запрещено предлагать вакансии, нарушающие законы и нормы."
                         "\n\n"
                         "🛑Любые вакансии, связанные с противозаконной деятельностью, такой как проституция, наркоторговля "
                         "и другие незаконные виды бизнеса, не допускаются."
                         "\n\n"
                         "🛑Публикация вакансий, представляющих собой явный спам или обман, например, заведомо ложные "
                         "предложения с высокими зарплатами, не допускается."
                         "\n\n"
                         "🛑Вакансии, которые могут представлять угрозу безопасности соискателей (например, неконтролируемое "
                         "сбор личной информации), строго запрещены."
                         "\n\n"
                         "🛑Работа, связанная с пирамидальными схемами, многократным маркетингом (MLM) или подобными "
                         "структурами, которые могут представлять финансовые риски для соискателей, не допускается."
                         "\n\n"
                         "🛑Если ваша реклама относится к этим критериям то ваша публикация не будет опубликован и средства возврату не подлежит!"
                         "\n\n\n"
                         "Благодарим за внимание и понимание!🙂\n"
                         "Мы ценим ваше соблюдение правил и желаем приятного взаимодействия с ботом.✅")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(support, commands=['support'])
    dp.register_message_handler(rule, commands=['rules', 'правила'])
