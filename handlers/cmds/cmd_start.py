import datetime

from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

reg_date = []


@router.message(CommandStart())
async def process_start(message: types.Message):
    reg_date.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    await message.answer(
        text=f'👋 Привет, {message.from_user.first_name}! Надеюсь тебе у нас понравится )\n\n'
             f'Используй команду /menu чтобы открыть меню.',
    )
