from aiogram.types import InlineKeyboardMarkup

from keyboards.common import back_to_menu_btn


def add_back_button(original_kb: InlineKeyboardMarkup) -> InlineKeyboardMarkup:
    new_keyboard = [row for row in original_kb.inline_keyboard]
    new_keyboard.append([back_to_menu_btn])

    return InlineKeyboardMarkup(inline_keyboard=new_keyboard)