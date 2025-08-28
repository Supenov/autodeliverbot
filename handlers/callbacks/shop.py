from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.shop import shop_kb
from keyboards.utils import add_back_button

rt = Router()

@rt.callback_query(F.data == 'shop')
async def open_shop(callback: CallbackQuery):
    # Добавляем кнопку "Назад в меню" к клавиатуре магазина
    enhanced_kb = add_back_button(shop_kb)

    await callback.message.edit_text(
        "🛍 Добро пожаловать в магазин! Выберите товар:",
        reply_markup=enhanced_kb
    )
    await callback.answer()