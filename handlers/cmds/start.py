import datetime

from aiogram import Router, types
from aiogram.filters import CommandStart

from keyboards.start_kb import keyboard as start_kb

rt = Router()

reg_date = []


@rt.message(CommandStart())
async def say_hello(message: types.Message):
    reg_date.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    await message.answer(text=f'👋 Приветствую, {message.from_user.first_name}! Надеюсь тебе у нас понравится )',
                         reply_markup=start_kb)
