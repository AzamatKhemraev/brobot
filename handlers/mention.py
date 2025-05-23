from aiogram import Router, types
from services.gpt import chat_with_gpt
from services.context import add_to_history, get_history
from database.user_service import get_users_by_chat
import asyncio

router = Router()

BOT_ALIASES = ["@bro", "@brobot", "bro", "brobot"]


@router.message()
async def mention_gpt_reply(message: types.Message):
    text = (message.text or "").lower()

    user_id = message.from_user.id
    username = message.from_user.username or None
    full_name = message.from_user.full_name

    if any(alias in text for alias in BOT_ALIASES):
        asyncio.create_task(respond_with_gpt(message))
    else:
        # Сохраняем обычное сообщение пользователя
        add_to_history(
            chat_id=message.chat.id,
            user_id=user_id,
            username=username,
            full_name=full_name,
            role="user",
            content=message.text
        )


async def respond_with_gpt(message: types.Message):
    try:
        chat_id = message.chat.id

        user_id = message.from_user.id
        username = message.from_user.username or None
        full_name = message.from_user.full_name

        # Добавим текущий вопрос пользователя в историю
        add_to_history(
            chat_id=chat_id,
            user_id=user_id,
            username=username,
            full_name=full_name,
            role="user",
            content=message.text
        )

        # Получаем последние 50 сообщений
        history = get_history(chat_id)

        # Получаем пользователей чата
        users = await get_users_by_chat(chat_id)

        # Формируем пролог и историю в виде текста
        prompt_text = format_history_prompt(history, users)

        # Отправка GPT
        gpt_reply = await chat_with_gpt([
            {"role": "system", "content": "Ты — дружелюбный ИИ, который помогает участникам чата. Они — твои друзья. Пиши кратко, понятно, дружелюбно, по делу."},
            {"role": "user", "content": prompt_text}
        ])

        # Сохраняем ответ в историю
        add_to_history(
            chat_id=chat_id,
            user_id=0,
            username=None,
            full_name="🤖",
            role="assistant",
            content=gpt_reply
        )

        if not isinstance(gpt_reply, str) or not gpt_reply.strip():
            gpt_reply = "🤖 Нейросеть ничего не ответила. Попробуй ещё раз позже."

        await message.reply(gpt_reply)

    except Exception as e:
        await message.reply(f"❗ Ошибка при ответе от GPT:\n`{e}`", parse_mode="Markdown")


def format_history_prompt(history, users):
    # Собираем список участников
    # unique_users = {msg["user_id"]: msg for msg in history if msg["role"] == "user"}

    intro = "Это групповой чат лучших друзей и ты один из них, со всеми разговаривай на ты. Участники:\n" + "\n".join(
        f"- {u['full_name']} (@{u['username']})" if u['username'] else f"- {u['full_name']}"
        for u in users
    ) + "\n\nИстория сообщений:\n"

    dialogue = "\n".join(
        f"{msg['full_name']}: {msg['content']}" for msg in history
    )

    return intro + dialogue


def register_handlers(dp):
    dp.include_router(router)
