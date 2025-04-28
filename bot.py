from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import register_handlers

import asyncio


async def main():
    # Создаём экземпляр бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем маршруты
    register_handlers(dp)

    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
