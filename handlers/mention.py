from aiogram import Router, types
from services.gpt import chat_with_gpt
# import asyncio

router = Router()

BOT_ALIASES = ["@bro", "@brobot", "bro", "brobot"]


@router.message()
async def mention_gpt_reply(message: types.Message):
    text = (message.text or "").lower()

    # Проверяем, есть ли упоминание
    if any(alias in text for alias in BOT_ALIASES):
        await message.bot.send_chat_action(message.chat.id, "typing")

        # GPT-ответ через OpenRouter
        gpt_reply = await chat_with_gpt(text)

        await message.reply(gpt_reply)


def register_handlers(dp):
    dp.include_router(router)
