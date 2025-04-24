from aiogram import Router, types
from services.gpt import chat_with_gpt
import asyncio

router = Router()

BOT_ALIASES = ["@bro", "@brobot", "bro", "brobot"]


@router.message()
async def mention_gpt_reply(message: types.Message):
    text = (message.text or "").lower()

    # Проверяем, есть ли упоминание
    if any(alias in text for alias in BOT_ALIASES):
        # запускаем асинхронную задачу в фоне
        asyncio.create_task(respond_with_gpt(message))


# эта функция отвечает GPT "в фоне"
async def respond_with_gpt(message: types.Message):
    try:
        await message.bot.send_chat_action(message.chat.id, "typing")
        gpt_reply = await chat_with_gpt(message.text)
        await message.reply(gpt_reply)
    except Exception as e:
        await message.reply(f"❗ Ошибка при ответе от GPT: {e}")


def register_handlers(dp):
    dp.include_router(router)
