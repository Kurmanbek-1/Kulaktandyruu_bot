from aiogram import Dispatcher, types
from config import Admins
import buttons

blocked_users = {}


#--------------------------------------------------------------------------------------------------------------------------

async def start(message: types.Message):
    user_id = message.from_user.id
    if message.from_user.id in Admins:
        await message.answer("🚀 О Нас:\n\n"
                            "Добро пожаловать в Kulaktandyruu👋\n"
                            "Моя цель - сделать этот процесс максимально простым для вас."
                            "\n\n"
                            "💳 Платежи:\n"
                            "У меня простая система оплаты.\n\n"
                            "🤖 Техподдержка:\n"
                            "Мы на связи 24/7. Пиши, и мы поможем!\n\n"
                            "📌Внимание!\n"
                            "Обязательно прочтите правила перед использованием бота!\n\n"
                            "⚠️ Важно!\n"
                            "Нецелевые сообщения могут быть автоматически заблокированы.\n\n"
                            "Благодарим за понимание! 🚀✨\n\n",
                             reply_markup=buttons.StartForAdmin)

    else:
        if user_id in blocked_users:
            await message.reply('Извините, вы заблокированы. 🚫', reply_markup=None)
            return
        else:
            await message.answer("🚀 О Нас:\n\n"
                            "Добро пожаловать в Kulaktandyruu👋\n"
                            "Моя цель - сделать этот процесс максимально простым для вас."
                            "\n\n"
                            "💳 Платежи:\n"
                            "У меня простая система оплаты.\n\n"
                            "🤖 Техподдержка:\n"
                            "Мы на связи 24/7. Пиши, и мы поможем!\n\n"
                            "📌Внимание!\n"
                            "Обязательно прочтите правила перед использованием бота!\n\n"
                            "⚠️ Важно!\n"
                            "Нецелевые сообщения могут быть автоматически заблокированы.\n\n"
                            "Благодарим за понимание! 🚀✨\n\n",
                                 reply_markup=buttons.OrderForStart)


async def support(message: types.Message):
    await message.answer('Наша тех.поддержка:\n'
                         '@kulaktandyruu_Bishkek', reply_markup=buttons.Start)

#--------------------------------------------------------------------------------------------------------------------------

async def rule(message: types.Message):
    user_id = message.from_user.id

    if user_id in blocked_users:
        await message.reply('Извините, вы заблокированы. 🚫', reply_markup=None)
        return
    else:
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

#--------------------------------------------------------------------------------------------------------------------------

async def block_user_by_id(message: types.Message):
    if message.from_user.id not in Admins:
        await message.reply('У вас нет прав на выполнение этой команды.')
        return

    try:
        user_id_to_block = int(message.text.split(' ')[1])
    except IndexError:
        await message.reply('Используйте команду в формате /block_user <user_ID> или /Заблокировать <user_ID>')
        return
    except ValueError:
        await message.reply('ID пользователя должен быть числом.')
        return

    blocked_users[user_id_to_block] = True
    await message.reply(f'Пользователь {user_id_to_block} заблокирован❗️')

#--------------------------------------------------------------------------------------------------------------------------

async def unblock_user_by_id(message: types.Message):
    if message.from_user.id not in Admins:
        await message.reply('У вас нет прав на выполнение этой команды.')
        return

    try:
        user_id_to_unblock = int(message.text.split(' ')[1])
    except IndexError:
        await message.reply('Используйте команду в формате /unblock_user <user_ID> или /Разблокировать <user_ID>')
        return
    except ValueError:
        await message.reply('ID пользователя должен быть числом.')
        return

    if blocked_users.get(user_id_to_unblock):
        del blocked_users[user_id_to_unblock]
        await message.reply(f'Пользователь {user_id_to_unblock} разблокирован. ✅')
    else:
        await message.reply(f'Пользователь {user_id_to_unblock} не был заблокирован.')

#--------------------------------------------------------------------------------------------------------------------------

async def show_blocked_users(message: types.Message):
    if message.from_user.id not in Admins:
        await message.reply('У вас нет прав на выполнение этой команды.')
        return

    if blocked_users:
        blocked_users_list = "\n".join(str(user_id) for user_id in blocked_users.keys())
        await message.reply(f'Заблокированные пользователи:\n{blocked_users_list}')
    else:
        await message.reply('Нет заблокированных пользователей.')

#--------------------------------------------------------------------------------------------------------------------------

async def info_for_block(message: types.Message):
    await message.answer(text="Инструкция по блокировке: ⬇️"
                         "\n\n"
                         "Блокировка: 🚫\n"
                         "/Заблокировать <user_ID>"
                         "\n\n"
                         "Разблокировка: ✅\n"
                         "/Разблокировать <user_ID>"
                         "\n\n"
                         "❗️Образец:\n"
                         "/Заблокировать 213121"
                         )

#--------------------------------------------------------------------------------------------------------------------------

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(support, commands=['support'])
    dp.register_message_handler(rule, commands=['rules', 'правила'])
    dp.register_message_handler(block_user_by_id, commands=['block_user', "Заблокировать"])
    dp.register_message_handler(unblock_user_by_id, commands=['unblock_user', "Разблокировать"])
    dp.register_message_handler(show_blocked_users, commands=['blocked_users', "Заблокированные!"])
    dp.register_message_handler(info_for_block, commands=['Инструкция!'])
