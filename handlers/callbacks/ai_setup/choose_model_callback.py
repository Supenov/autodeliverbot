from aiogram import F, Router, types



router = Router()


@router.callback_query(F.data == 'choose_model')
async def open_shop_callback(callback_data: types.CallbackQuery):
    await callback_data.message.answer(text='In development...')
