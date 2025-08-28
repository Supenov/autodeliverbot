from aiogram import types, Router, F

from keyboards.back_to_menu_kb import keyboard as back_to_menu_kb

from ..cmds.start import reg_date

rt = Router()


@rt.callback_query(F.data == 'user_profile')
async def user_profile_handler(callback_data: types.CallbackQuery):
    await callback_data.message.edit_text(text=f"""
    ✨ Добро пожаловать в ваш профиль! ✨
    🔹 Имя: {callback_data.from_user.first_name}
    🔹 ID: <code>{callback_data.from_user.id}</code>
    🔹 Уровень: ... ⭐
    🔹 Баланс: ... ₽
    🔹 Дата регистрации: {reg_date[0]}
    
Вы с нами уже ... дней — спасибо за доверие! 💖
    """,
                                          reply_markup=back_to_menu_kb)
