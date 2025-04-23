from aiogram import Router, types
import asyncio

router = Router()


@router.message()
async def reply_if_mentioned(message: types.Message):
    text = message.text or ""

    # Проверка по имени напрямую
    if "@bro" in text.lower() or "brobot" in text.lower():
        await message.bot.send_chat_action(message.chat.id, "typing")
        await asyncio.sleep(1)
        await message.reply("👋 Я тут! Ты звал меня?")


def register_handlers(dp):
    dp.include_router(router)
