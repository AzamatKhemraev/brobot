from aiogram import Router, types
from services.gpt import chat_with_gpt
import asyncio

router = Router()

BOT_ALIASES = ["@bro", "@brobot", "bro", "brobot"]


@router.message()
async def mention_gpt_reply(message: types.Message):
    text = (message.text or "").lower()

    if any(alias in text for alias in BOT_ALIASES):
        asyncio.create_task(respond_with_gpt(message))


async def respond_with_gpt(message: types.Message):
    try:
        gpt_reply = await chat_with_gpt(message.text)

        # 💡 Защита от None — если GPT не вернул ничего
        if not isinstance(gpt_reply, str) or not gpt_reply.strip():
            gpt_reply = "🤖 Нейросеть ничего не ответила. Попробуй ещё раз позже."

        await message.reply(gpt_reply)

    except Exception as e:
        await message.reply(f"❗ Ошибка при ответе от GPT:\n`{e}`", parse_mode="Markdown")


def register_handlers(dp):
    dp.include_router(router)
