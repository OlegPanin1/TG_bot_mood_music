import logging
from aiogram import Bot, Dispatcher, types, executor
import os

# Настройка логгера (AI-агент мониторинга)
logging.basicConfig(
    filename='error.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.ERROR
)

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    try:
        await message.answer("Привет! 🎶 Я музыкальный бот. Напиши, какое у тебя настроение.")
    except Exception as e:
        logging.error(f"Ошибка при обработке /start: {e}")

if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")
