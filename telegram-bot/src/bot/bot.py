import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.models import async_session, UserMessage, Base, engine

import dotenv
dotenv.load_dotenv()
API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def get_inline_keyboard():
    builder = InlineKeyboardBuilder()
    for i in range(1, 11):
        builder.button(text=f"Set {i}", callback_data=f"set:{i}")
    builder.adjust(3, 2)
    return builder.as_markup()

@dp.message(F.text)
async def handle_text(msg: Message):
    async with async_session() as session:
        session.add(UserMessage(user_id=msg.from_user.id, message_text=msg.text))
        await session.commit()
    await msg.answer("✅ Saved to DB!", reply_markup=get_inline_keyboard())

@dp.callback_query(F.data.startswith("set:"))
async def handle_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"You selected option {callback.data.split(':')[1]}")

async def main():
    import sys

    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())