import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import executor

API_TOKEN = '6749577684:AAGUrE2L-INm8dunF9DdNtw-_6wrcLQAT1M'

# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Определение команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Привет, для авторизации введи код: ")

if __name__ == '__main__':
    # Запуск бота
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)