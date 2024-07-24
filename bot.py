import asyncio
from aiogram import Dispatcher, Bot, types, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from decouple import config
from config import client
TOKEN = '7387769280:AAHcpy_pXNIHQIYF_cV3B8i-d7Y7GlT8RRY'
user_name = ""


bot = Bot(token=TOKEN)
dp = Dispatcher()

#Стартовое меню
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Добрый день')
    user_name=message.from_user.full_name
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


#Создание новых ключей  доступа через API запрос
@dp.callback_query(F.data == "1_month_sub")
async def create_1_month_sub(callback: types.CallbackQuery):
    new_key_info = create_new_key(name=user_name, data_limit_gb=1.5)
    await callback.message.answer("Вы успешно оформили подписку на 1 месяц")


#Запуск бота
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Извините, бот временно недоступен!")
        
        
#Функция преобразования Гигабайтов в байты
def gb_to_bytes(gb: float):
    bytes_in_gb = 1024 ** 3  
    return int(gb * bytes_in_gb)

#Получение информации о всех ключах
def get_keys():
    return client.get_keys()

#Получение информации по конкретному ключу
def get_key_info(key_id: str):
    return client.get_key(key_id)

#Создание нового ключа без ограничений
def create_new_key(key_id: str = None, name: str = None, data_limit_gb: float = None):
    return client.create_key(key_id=key_id, name=name, data_limit=gb_to_bytes(data_limit_gb))