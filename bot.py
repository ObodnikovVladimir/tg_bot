import asyncio
from aiogram import Dispatcher, Bot, types, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import os
import decouple
from config import client


TOKEN = '7387769280:AAHcpy_pXNIHQIYF_cV3B8i-d7Y7GlT8RRY'


bot = Bot(token=TOKEN)
dp = Dispatcher()

# Стартовое меню
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer('Добрый день')
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("Оформить подписку", callback_data="create_subscription"),
        InlineKeyboardButton("Узнать статус подписки", callback_data="info_subscription")
    )
    await message.answer("Хотите получить доступ к заблокированным сервисам?", reply_markup=markup)

# Ответы из меню
@dp.callback_query_handler(lambda callback: callback.data == "create_subscription")
async def create_subscription(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("1 месяц", callback_data="1_month_sub"),
        InlineKeyboardButton("3 месяца", callback_data="3_month_sub")
    )
    await callback.message.answer("На сколько хотите оформить подписку?", reply_markup=markup)

# Создание новых ключей доступа через API запрос
@dp.callback_query_handler(lambda callback: callback.data == "1_month_sub")
async def create_1_month_sub(callback: types.CallbackQuery):
    key_info = get_key_info("100")
    await callback.message.answer(f"Вы успешно оформили подписку на 1 месяц {key_info}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Извините, бот временно недоступен!")

# Функция преобразования Гигабайтов в байты
def gb_to_bytes(gb: float):
    bytes_in_gb = 1024 ** 3
    return int(gb * bytes_in_gb)

# Получение информации о всех ключах
def get_keys():
    return client.get_keys()

# Получение информации по конкретному ключу
def get_key_info(key_id: str):
    return client.get_key(key_id)
