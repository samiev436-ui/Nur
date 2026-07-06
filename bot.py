import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")  # URL панели VPN
API_KEY = os.getenv("API_KEY")  # ключ API панели

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я VPN‑бот.\n\n"
        "Я могу выдавать VPN‑доступ, показывать тарифы и принимать оплату.\n\n"
        "Выбери действие:\n"
        "/buy — купить VPN\n"
        "/info — информация\n"
        "/help — помощь"
    )


@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await message.answer("ℹ️ Информация о VPN:\n\n• Быстрый\n• Защищённый\n• Работает в РФ\n• Поддержка Telegram")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("❓ Помощь:\n\nЕсли что-то не работает — напиши сюда.")


@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    await message.answer(
        "💳 Купить VPN:\n\n"
        "Пока что оплата вручную.\n"
        "Когда подключим Stars/CryptoBot — будет автоматически.\n\n"
        "После оплаты я выдам конфиг."
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
