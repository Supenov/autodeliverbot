from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура магазина
shop_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎁 Товар 1", callback_data="buy_1"),
            InlineKeyboardButton(text="⭐ Товар 2", callback_data="buy_2")
        ],
        [
            InlineKeyboardButton(text="🛒 Все товары", callback_data="all_products")
        ]
    ]
)