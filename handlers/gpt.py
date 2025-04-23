from aiogram import Router, types
from aiogram.filters import Command
from services.gpt import chat_with_gpt
import asyncio

router = Router()


@router.message(Command("ask"))
async def ask_gpt(message: types.Message):
    prompt = message.text.removeprefix("/ask").strip()

    if not prompt:
        await message.reply("❗ Напиши свой вопрос после /ask. Пример:\n`/ask Что такое сингулярность?`", parse_mode="Markdown")
        return

    await message.bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1)

    gpt_reply = await chat_with_gpt(prompt)
    await message.reply(gpt_reply, disable_web_page_preview=True)


def register_handlers(dp):
    dp.include_router(router)
