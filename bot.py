import asyncio
from aiogram import Dispatcher, Bot, types, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random
import os

TOKEN = '7387769280:AAHcpy_pXNIHQIYF_cV3B8i-d7Y7GlT8RRY'


bot = Bot(token=TOKEN)
dp = Dispatcher()

#Стартовое меню
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Добрый день')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Оформить подписку",
        callback_data="create_subscription")
    )
    builder.add(types.InlineKeyboardButton(
        text="Узнать статус подписки",
        callback_data="info_subscription")
    )
    await message.answer("Хотите получить доступ к заблокированным сервисам?", reply_markup=builder.as_markup())
    
#Ответы из меню
@dp.callback_query(F.data == "create_subscription")
async def create_subscription(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="1 месяц",
        callback_data="1_month_sub")
    )
    builder.add(types.InlineKeyboardButton(
        text="3 месяца",
        callback_data="3_month_sub")
    )
    await callback.message.answer("На сколько хотите оформить подписку?", reply_markup=builder.as_markup())


#Запуск бота
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Извините, бот временно недоступен!")