from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

return_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='⬅️ Назад в меню', callback_data='return_to_menu')],
    ]
)
