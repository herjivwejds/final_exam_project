from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import aiohttp  # Asinxron HTTP so'rovlar uchun
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7689593005:AAH9Dg7dC2zkldSZxjjKHg8og5O7own0IJQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Menyu tugmalari
menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Menyu")],
        [KeyboardButton(text="ℹ️ Biz haqimizda"), KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)

# /start komandasi
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    telegram_id = message.from_user.id
    full_name = message.from_user.full_name

    async with aiohttp.ClientSession() as session:
        # Django APIga foydalanuvchini yuborish
        async with session.post("http://localhost:8000/api/register/", json={
            "telegram_id": telegram_id,
            "full_name": full_name
        }) as response:
            if response.status == 200:
                await message.answer("Siz imtihon uchun tayyorlanmoqdasiz", reply_markup=menu_buttons)
            else:
                await message.answer("Foydalanuvchi ro'yxatdan o'tishda xato yuz berdi.")

# Tugmalar bosilganda javob berish
@dp.message_handler(lambda message: message.text == "ℹ️ Biz haqimizda")
async def about(message: types.Message):
    await message.answer("Biz imtihon uchun Telegram bot yaratmoqdamiz 😊")

@dp.message_handler(lambda message: message.text == "📞 Aloqa")
async def contact(message: types.Message):
    await message.answer("Aloqa: @admin_username")

@dp.message_handler(lambda message: message.text == "📋 Menyu")
async def show_menu(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8000/api/products/") as response:
            products = await response.json()

    if not products:
        await message.answer("Hozircha menyuda taomlar yo‘q.")
    else:
        for product in products:
            keyboard = InlineKeyboardMarkup().add(
                InlineKeyboardButton(text=f"{product['price']} so'm", callback_data=f"buy_{product['id']}")
            )
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=product['image'],
                caption=product['name'],
                reply_markup=keyboard
            )

# Botni ishga tushurish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
