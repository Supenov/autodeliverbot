from aiogram import Router, types
from aiogram.filters import Command

from keyboards.menu_keyboard import menu_keyboard

router = Router()

text = f'''[YOCBAI v1.0] • АКТИВЕН
────────────────────────────
▸ Режим: Чат с ИИ
▸ Статус: Онлайн
▸ Модель: NeuralNet-7B
▸ Температура: 0.8

Доступные команды:
• /chat — начать диалог
• /generate — сгенерировать текст
• /analyze — анализ
────────────────────────────'''


@router.message(Command('menu'))
async def process_menu(message: types.Message):
    await message.answer(
        text=text,
        reply_markup=menu_keyboard,
    )
