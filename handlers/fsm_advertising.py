from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from config import bot, Admins
from keyboards import buttons

# =======================================================================================================================

user_id = None


class advertising(StatesGroup):
    info = State()
    submit = State()
    info_tariff_file = State()
    info_photo = State()
    tariff = State()
    social_network = State()
    photo_check = State()
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
    await message.answer('Хотите отправить файл или фотку?', reply_markup=buttons.fileorphoto)


async def fileorphotoreklama(message: types.Message):
    if message.text == "Хочу отправить файл!":
        await advertising.info_tariff_file.set()
        await message.answer("Отправьте файл!")

    elif message.text == 'Хочу отправить фотку!':
        await advertising.info_photo.set()
        await message.answer("Отправьте фотографию/картинку!")

    else:
        photo_tariff = open('media/img.png', 'rb')
        await advertising.tariff.set()
        await message.answer_photo(photo=photo_tariff, caption="Какой тариф вы хотите выбрать? ⬇️",
                                   reply_markup=buttons.cancel_markup)


async def process_tariff_file_load(message: types.Message, state: FSMContext):
    # Получение информации о файле
    file_id = message.document.file_id
    file_size = message.document.file_size
    file_name = message.document.file_name

    # Загрузка файла
    file = await bot.get_file(file_id)
    file_path = file.file_path

    # Обработка файла, например, сохранение его локально
    bytes_io = await bot.download_file(file_path)

    # Определение пути для сохранения файла в папке "files"
    file_path_to_save = os.path.join('files', file_name)

    # Сохранение файла локально
    with open(file_path_to_save, 'wb') as file_local:
        file_local.write(bytes_io.getvalue())

    # Сохранение информации о файле в состоянии
    async with state.proxy() as data:
        data['tariff_file_path'] = file_path_to_save

    photo_tariff = open('media/img.png', 'rb')
    await advertising.tariff.set()
    await message.answer_photo(photo=photo_tariff, caption="Какой тариф вы хотите выбрать? ⬇️")


async def info_photo_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_photo'] = message.photo[-1].file_id

    photo_tariff = open('media/img.png', 'rb')
    await advertising.tariff.set()
    await message.answer_photo(photo=photo_tariff, caption="Какой тариф вы хотите выбрать? ⬇️")


async def tariff(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tariff'] = message.text
    await advertising.next()
    await message.answer("Где хотите запустить рекламу?")


async def social_network(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['social_network'] = message.text
    photo_requisites = open('media/img_1.png', 'rb')

    await message.answer_photo(photo=photo_requisites,
                               caption='Вот реквизиты на которые нужно перевести деньги для оплаты! 📨')
    await advertising.next()
    await message.answer(f"Отправьте фотку/скриншот чека!")


async def process_receipt(message: types.Message, state: FSMContext):
    global user_id
    async with state.proxy() as data:
        data["photo_check"] = message.photo[-1].file_id

    user_id = message.chat.id

    await send_admin_data(user_id, data)

    await message.answer("Отправлено на проверку администратору!  🙌🏼\n"
                         "Это займет какое-то время, прошу подождать! ⏳")
    await state.finish()


async def send_admin_data(user_id, data):
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    button_yes = InlineKeyboardButton("Да✅", callback_data="button_yes")
    button_no = InlineKeyboardButton("Нет❌", callback_data="button_no")
    inline_keyboard.add(button_yes, button_no)

    for Admin in Admins:
        await bot.send_photo(
            photo=data['photo_check'],
            chat_id=Admin,
            caption=f"Поступил новый заказ от пользователя с ID {user_id}", reply_markup=inline_keyboard)

        if 'tariff_file_path' in data:
            with open(data['tariff_file_path'], 'rb') as file:
                await bot.send_document(chat_id=Admin, document=file)

        elif 'info_photo' in data:
            await bot.send_photo(chat_id=Admin, photo=data['info_photo'])


async def answer_yes(message: types.Message):
    global user_id
    await bot.send_message(user_id, text="Оплата прошла успешно! Спасибо за ваш заказ. ✅")

    for Admin in Admins:
        await bot.send_message(chat_id=Admin, text='Подтверждено! ✅')


async def answer_no(message: types.Message):
    global user_id
    await bot.send_message(user_id,
                           text="Оплата не прошла. Пожалуйста, свяжитесь с поддержкой для дополнительной информации. ❌")
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
    dp.register_message_handler(process_tariff_file_load, state=advertising.info_tariff_file,
                                content_types=['document'])
    dp.register_message_handler(info_photo_load, state=advertising.info_photo, content_types=['photo'])
    dp.register_message_handler(tariff, state=advertising.tariff)
    dp.register_message_handler(social_network, state=advertising.social_network)
    dp.register_message_handler(process_receipt, state=advertising.photo_check, content_types=['photo'])
    dp.register_message_handler(send_admin_data, state=advertising.send_admin)

    dp.register_callback_query_handler(answer_yes, lambda call: call.data == "button_yes")
    dp.register_callback_query_handler(answer_no, lambda call: call.data == "button_no")
