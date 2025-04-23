from aiogram import Bot, Dispatcher
# from aiogram.types import ParseMode
from config import BOT_TOKEN
from handlers import echo, gpt, mention, gif, sticker_id_catcher

import asyncio


async def main():
    # Создаём экземпляр бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем маршруты
    echo.register_handlers(dp)
    gpt.register_handlers(dp)
    mention.register_handlers(dp)
    gif.register_handlers(dp)
    sticker_id_catcher.register_handlers(dp)

    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
