import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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



@dp.message(F.text == "/start")
async def handle_start(msg: Message):
    await msg.answer("Привіт! 👋\nНатисни кнопку нижче, щоб поговорити зі мною 😊", reply_markup=get_reply_keyboard_hello())


@dp.message(F.text.in_([
    "Привіт",
    "єВідновлення",
    "Соціальна підтримка",
    "ВПО",
    "Субсидії",
    "Притулок"
]))
async def handle_dialogflow_query(msg: Message):
    import requests
    print("handle_dialogflow_query")
    try:
        payload = {
            "query":  msg.text
        }

        url = "http://26.94.179.143:8001/api/v1/dialogflow"

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        message = response.json()["answer"]
    except Exception as e:
        message = f"❌ Помилка при запиті: {e}"

    await msg.answer(message, reply_markup=get_reply_keyboard_topics())


@dp.message()
async def handle_free_text(msg: Message):
    import requests

    base_url = "http://127.0.0.1:8000/create_summarized_answer/"
    params = {
        "query": msg.text
    }
    headers = {
        "accept": "application/json"
    }

    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        message = data.get("answer", "🤖 Немає відповіді від сервісу")
    except Exception as e:
        message = f"❌ Помилка при запиті: {e}"

    await msg.answer(message, reply_markup=get_reply_keyboard_topics())


def get_reply_keyboard_hello() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Привіт")
    builder.adjust(1) 
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def get_reply_keyboard_topics() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()


    topics = [
        "єВідновлення",
        "Соціальна підтримка",
        "ВПО",
        "Субсидії",
        "Притулок",
    ]
    for topic in topics:
        builder.button(text=topic)

    builder.adjust(2) 
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)



# def get_reply_keyboard_topic_options() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()

#     builder.button(text="👋 Привітання")

#     topics = [
#         "Хочу отримати файл",
#         "Поясни мені...",
#     ]
#     for topic in topics:
#         builder.button(text=topic)

#     builder.adjust(2) 
#     return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)




async def main():
    import sys

    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())