from aiogram import types
from aiogram.fsm.context import FSMContext

import tgbot.keyboards.__init__ as kb


async def start_command_handler(message: types.Message, state: FSMContext):
    from_user = message.from_user

    greeting_text = f"С возвращением, {from_user.full_name}! Чем могу помочь?"

    await message.answer(greeting_text, reply_markup = kb.main)
