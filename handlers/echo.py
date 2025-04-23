from aiogram import Router, types
from aiogram.filters import Command
import asyncio

# Создаём роутер
router = Router()


# Обработка команды /echo
@router.message(Command("echo"))
async def echo_cmd(message: types.Message):
    # Бот показывает, что "печатает"
    await message.bot.send_chat_action(message.chat.id, action="typing")

    # Задержка, будто бот печатает
    await asyncio.sleep(3)  # 2 секунды — можешь настроить

    # Отправка самого сообщения
    await message.reply("Дич сук")


# Функция для регистрации хендлеров
def register_handlers(dp):
    dp.include_router(router)
