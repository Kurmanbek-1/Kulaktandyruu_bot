from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# ======================================================================================================================
StartForAdmin = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('/all_advertising'))

Social_Network = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('TikTok'),
                                          KeyboardButton('Instagram'))

cancel_button = KeyboardButton('Отмена')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    ).add(cancel_button)

submit_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('Да'),
                                          KeyboardButton('Нет'))

fileorphoto = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('Хочу отправить фотку!'),
                                          KeyboardButton('Нет, не хочу!'))
# ======================================================================================================================
back = KeyboardButton('/<назад')
# ======================================================================================================================
yesno = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2).add(KeyboardButton('Да'),
                     KeyboardButton('Нет'),
                     cancel_button)

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True).add(KeyboardButton(''))