import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import Message

TOKEN = "7387769280:AAHcpy_pXNIHQIYF_cV3B8i-d7Y7GlT8RRY"


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message):
    await message.answer('Добрый день')
    await message.reply('Хотите получить доступ к заблокированным сервисам?')

async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Извините, бот временно недоступен!")