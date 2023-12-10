from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot, Admins
from keyboards import buttons


# =======================================================================================================================

class advertising(StatesGroup):
    info = State()
    social_network = State()
    submit = State()


async def fsm_start(message: types.Message):
    await advertising.info.set()
    await message.answer("Выберите город:", reply_markup=buttons)


async def info(message: types.Message, state: FSMContext):
    selected_city = message.text
    await state.update_data(city=selected_city)
    await advertising.social_network.set()
    await message.answer("Где хотите запустить рекламу?")



async def social_network(message: types.Message, state: FSMContext):
    selected_city = message.text
    await message.answer(f"Верно?", reply_markup=buttons.submit_markup)





async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start)


# =======================================================================================================================
def register_all_products(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals="Отмена", ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=["Товары!"])
    dp.register_message_handler(info, state=advertising.info)
    dp.register_message_handler(social_network, state=advertising.social_network)
