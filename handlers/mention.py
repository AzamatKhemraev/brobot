from aiogram import Router, types
from services.gpt import chat_with_gpt
from services.context import add_to_history, get_history
import asyncio

router = Router()

BOT_ALIASES = ["@bro", "@brobot", "bro", "brobot"]


@router.message()
async def mention_gpt_reply(message: types.Message):
    text = (message.text or "").lower()

    if any(alias in text for alias in BOT_ALIASES):
        asyncio.create_task(respond_with_gpt(message))
    else:
        # Сохраняем просто как user-реплику
        add_to_history(message.chat.id, "user", message.text or "")


async def respond_with_gpt(message: types.Message):
    try:
        chat_id = message.chat.id

        # Добавим текущий вопрос пользователя в историю
        add_to_history(chat_id, "user", message.text)

        # Получаем последние 50 сообщений
        history = get_history(chat_id)

        # Добавим system prompt в начало
        prompt = [{"role": "system", "content": "Ты робот помошник. Твоя задача коротко и по существу отвечать на вопросы. Используй нейтральный стиль общения."}] + history

        gpt_reply = await chat_with_gpt(prompt)

        # Сохраняем ответ в историю
        add_to_history(chat_id, "assistant", gpt_reply)

        # 💡 Защита от None — если GPT не вернул ничего
        if not isinstance(gpt_reply, str) or not gpt_reply.strip():
            gpt_reply = "🤖 Нейросеть ничего не ответила. Попробуй ещё раз позже."

        await message.reply(gpt_reply)

    except Exception as e:
        await message.reply(f"❗ Ошибка при ответе от GPT:\n`{e}`", parse_mode="Markdown")


def register_handlers(dp):
    dp.include_router(router)
