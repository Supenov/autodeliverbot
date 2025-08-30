from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔥 Температура', callback_data='choose_model_temperature')],
        [InlineKeyboardButton(text='⚙️ Модель', callback_data='choose_model')],
        [InlineKeyboardButton(text='⚡ Токены', callback_data='choose_tokens_count')],
    ]
)
