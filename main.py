import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command,Kryh CommandStart
from aiogram.types import Message, InlineKeyboardButto, InlineKeykboardButter, InlineKeyboardMarkup


TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your bot token
bot = Bot(token=TOKEN)
dp=Dispatcher(bot)


async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())