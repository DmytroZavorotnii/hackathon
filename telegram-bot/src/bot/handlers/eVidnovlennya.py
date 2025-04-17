from aiogram import F, types
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from ..bot import dp

eVidnovlennya_menu = InlineKeyboardMarkup(
    keyboard=[
        [InlineKeyboardButton(text="Отримати пораду", callback_data="advice")],
        [InlineKeyboardButton(text="Отримати документ", callback_data="document")],
    ]
)

@dp.callback_query(F.data == "eVidnovlennya")
async def eVidnovlennya_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        text=(
            "🔧 *єВідновлення* — це державна програма допомоги постраждалим від бойових дій.\n\n"
            "Оберіть доступні опції нижче 👇"
        ),
        reply_markup=eVidnovlennya_menu
    )
    await callback.answer()

@dp.callback_query(F.data == "advice")
async def advice_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        text=(
            "..."
        )
    )
    await callback.answer()

@dp.callback_query(F.data == "document")
async def document_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        text=(
            "Ви можете отримати інформацію щодо програми “єВідновлення” з офіційного вебпорталу "
            "Кабінету Міністрів України за посиланням:\n"
            "[єВідновлення](https://www.kmu.gov.ua/news/yevidnovlennya-vidnovlennya-zhitla-pislya-ruynuvannya-vnaslidok-viyni-rosiyi-proti-ukrayini) \n\n"
            "Ви також можете подати заявку на отримання допомоги через портал Дія:\n"
            "[Портал Дія](https://diia.gov.ua/services/categories/gromadyanam/yevidnovlennia) \n\n"
        ),
        parse_mode="Markdown"
    )
    await callback.answer()