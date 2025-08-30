from aiogram import F, Router, types

# ...

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


@router.callback_query(F.data == 'return_to_menu')
async def return_to_menu_callback(callback_data: types.CallbackQuery):
    await callback_data.message.edit_text(
        text=text
    )
