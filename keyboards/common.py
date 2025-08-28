from aiogram.types import InlineKeyboardButton

# Кнопка "Назад в меню"
back_to_menu_btn = InlineKeyboardButton(
    text="⬅️ Назад в меню",
    callback_data="main_menu"
)