from aiogram import F, Router, types

from handlers.cmds.cmd_start import reg_date
from keyboards.return_to_menu_keyboard import return_to_menu_keyboard

router = Router()


@router.callback_query(F.data == 'open_profile')
async def open_shop_callback(callback_data: types.CallbackQuery):
    if reg_date:
        await callback_data.message.edit_text(
            text=f'Логин: {callback_data.from_user.first_name}\n'
                 f'ID: {callback_data.from_user.id}\n'
                 f'Дата регистрации: {reg_date[0]}',
            reply_markup=return_to_menu_keyboard,
        )
    else:
        await callback_data.message.edit_text(
            text=f'Логин: {callback_data.from_user.first_name}\n'
                 f'ID: {callback_data.from_user.id}\n'
                 f'Дата регистрации: -',
            reply_markup=return_to_menu_keyboard,
        )
