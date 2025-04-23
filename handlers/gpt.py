from aiogram import Router, types
from aiogram.filters import Command
from services.gpt import chat_with_gpt
import asyncio

router = Router()


@router.message(Command("ask"))
async def ask_gpt(message: types.Message):
    prompt = message.text.removeprefix("/ask").strip()

    if not prompt:
        await message.reply("❗ Пожалуйста, напиши вопрос после команды /ask")
        return

    await message.bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1)

    try:
        gpt_reply = await chat_with_gpt(prompt)
        await message.reply(gpt_reply)
    except Exception as e:
        await message.reply(f"⚠️ Ошибка: {e}")


def register_handlers(dp):
    dp.include_router(router)
