from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import echo, mention, stickers

import asyncio


async def main():
    # Создаём экземпляр бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем маршруты
    echo.register_handlers(dp)
    mention.register_handlers(dp)
    stickers.register_handlers(dp)

    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
