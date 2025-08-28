from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='💰 Магазин', callback_data='shop'), InlineKeyboardButton(text='🔐 Профиль', callback_data='user_profile')],
        [InlineKeyboardButton(text='👽 Другое', callback_data='other')]
    ]
)