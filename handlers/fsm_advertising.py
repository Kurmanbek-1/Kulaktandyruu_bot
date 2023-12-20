from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from config import bot, Admins
from keyboards import buttons
from db.ORM import sql_insert_advertising

# =======================================================================================================================

user_id = None
username = None
fullname = None


class advertising(StatesGroup):
    info = State()  # 1
    submit = State()
    info_photo = State()  # 2
    tariff = State()  # 3
    social_network = State()  # 4
    photo_check = State()  # 5
    process_receipt = State()
    send_admin = State()
    submit_admin = State()


async def fsm_start(message: types.Message):
    await advertising.info.set()
    await message.answer("Раскажите о вашей рекламе!")


async def info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = message.text
    await advertising.next()
    await message.answer('Хотите отправить фотку, того что вы хотите чтоб мы прорекламировали?',
                         reply_markup=buttons.fileorphoto)


async def fileorphotoreklama(message: types.Message):
    if message.text == 'Хочу отправить фотку!':
        await advertising.info_photo.set()
        await message.answer("Отправьте фотографию/картинку!")

    elif message.text == 'Нет, не хочу!':
        photo_tariff = open('media/img.png', 'rb')
        await advertising.tariff.set()
        await message.answer_photo(photo=photo_tariff, caption="Какой тариф вы хотите выбрать? ⬇️",
                                   reply_markup=buttons.ButtonForSocialNetwork)

    else:
        await message.answer('Выберите что вы хотите отправить через кнокпи ⬇️', reply_markup=buttons.fileorphoto)


async def info_photo_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_photo'] = message.photo[-1].file_id

    photo_tariff = open('media/img.png', 'rb')
    await advertising.tariff.set()
    await message.answer_photo(photo=photo_tariff, caption="Какой тариф вы хотите выбрать? ⬇️",
                               reply_markup=buttons.ButtonForSocialNetwork)


async def tariff(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tariff'] = message.text
    await advertising.next()
    await message.answer("Где хотите запустить рекламу?\n"
                         "(Telegram уже включен в них!)", reply_markup=buttons.Social_Network)


async def social_network(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['social_network'] = message.text
    photo_requisites = open('media/img_1.png', 'rb')

    await message.answer_photo(photo=photo_requisites,
                               caption='Вот реквизиты на которые нужно перевести деньги для оплаты! 📨')
    await advertising.next()
    await message.answer(f"Отправьте фотку/скриншот чека!", reply_markup=buttons.cancel_markup)


async def process_receipt(message: types.Message, state: FSMContext):
    global user_id
    global fullname
    global username

    async with state.proxy() as data:
        data["photo_check"] = message.photo[-1].file_id

    user_id = message.chat.id
    fullname = message.chat.full_name
    username = message.chat.username

    await send_admin_data(data, state)

    await sql_insert_advertising(state)

    await message.answer("Отправлено на проверку администратору!  🙂\n"
                         "Это займет какое-то время, прошу подождать! ⏳", reply_markup=buttons.Start)
    await state.finish()


async def send_admin_data(data, state: FSMContext):
    global fullname
    global user_id
    global username

    if not username:
        username = fullname

    async with state.proxy() as data:
        data["user_id"] = user_id
        data["user_name"] = f"@{username}"

    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    button_yes = InlineKeyboardButton("Да✅", callback_data="button_yes")
    button_no = InlineKeyboardButton("Нет❌", callback_data="button_no")
    inline_keyboard.add(button_yes, button_no)

    caption = (f'Поступил новый заказ от пользователя с ID {user_id}\n\n'
               f'Информация: {data["info"]}\n'
               f'User_ID: {data["user_id"]}\n'
               f'Username: {data["user_name"]}\n'
               f'Тариф: {data["tariff"]}\n'
               f'Где нужно прорекламировать: {data["social_network"]}')

    for Admin in Admins:
        await bot.send_photo(
            photo=data['photo_check'],
            chat_id=Admin,
            caption=caption, reply_markup=inline_keyboard)

        if 'info_photo' in data:
            await bot.send_photo(chat_id=Admin, photo=data['info_photo'])


async def answer_yes(message: types.Message, state: FSMContext):
    global user_id
    await bot.send_message(user_id, text="Оплата прошла успешно! ✅\n "
                                         "Спасибо, что выбрали нас! Надеемся и дальше быть вам полезными! 🙂",
                           reply_markup=buttons.Start)

    for Admin in Admins:
        await bot.send_message(chat_id=Admin, text='Подтверждено! ✅')


async def answer_no(message: types.Message):
    global user_id
    await bot.send_message(user_id,
                           text="Оплата не прошла. ❌ \n"
                                "Пожалуйста, свяжитесь с поддержкой для дополнительной информации.\n"
                                "@kulaktandyruu_Bishkek", reply_markup=buttons.Start)
    for Admin in Admins:
        await bot.send_message(chat_id=Admin, text='Отклонено! ❌')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=None)


# =======================================================================================================================
def register_advertising(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals="Отмена", ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=["Заказать!", "order"])

    dp.register_message_handler(info, state=advertising.info)
    dp.register_message_handler(fileorphotoreklama, state=advertising.submit)

    dp.register_message_handler(info_photo_load, state=advertising.info_photo, content_types=['photo'])
    dp.register_message_handler(tariff, state=advertising.tariff)
    dp.register_message_handler(social_network, state=advertising.social_network)
    dp.register_message_handler(process_receipt, state=advertising.photo_check, content_types=['photo'])
    dp.register_message_handler(send_admin_data, state=advertising.send_admin)

    dp.register_callback_query_handler(answer_yes, lambda call: call.data == "button_yes")
    dp.register_callback_query_handler(answer_no, lambda call: call.data == "button_no")
