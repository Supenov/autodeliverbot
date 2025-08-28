from aiogram import Router, types, F

from keyboards.start_kb import keyboard as start_kb

rt = Router()


@rt.callback_query(F.data == 'main_menu')
async def say_hello(callback_data: types.CallbackQuery):
    await callback_data.message.edit_text(
        text=f'👋 Приветствую, {callback_data.from_user.first_name}! Надеюсь тебе у нас понравится )',
        reply_markup=start_kb)
