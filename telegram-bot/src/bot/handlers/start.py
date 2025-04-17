from aiogram import types, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from ..bot import bot, dp

# Основне меню
main_menu = InlineKeyboardMarkup(
    keyboard=[
        [InlineKeyboardButton(text="🏠 єВідновлення", callback_data="eVidnovlennya")],
        #[InlineKeyboardButton(text="📌 Часті питання"), ],
    ]
)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        text=(
            "Вітаємо в боті правової допомоги.\n\n"
            "Тут ви можете:\n"
            "• отримати відповіді та поради щодо обраної тематики, \n"
            "• отримати правові документи.\n\n"
            "Оберіть доступні теми нижче 👇"
        ),
        reply_markup=main_menu
    )
