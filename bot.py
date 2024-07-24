import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import Message
import os

TOKEN = '7387769280:AAHcpy_pXNIHQIYF_cV3B8i-d7Y7GlT8RRY'
user_name = ""


bot = Bot(token=TOKEN)
dp = Dispatcher()

#Стартовое меню
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Добрый день')
    await message.answer('Хотите получить доступ к заблокированным сервисам?')

async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Извините, бот временно недоступен!")