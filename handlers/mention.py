from aiogram import Router, types
from services.gpt import chat_with_gpt
from services.context import add_to_history, get_history
from database.user_service import get_users_by_chat, get_user
import asyncio
import random

router = Router()

BOT_ALIASES = ["@bro", "@brobot", "bro", "brobot"]


@router.message()
async def mention_gpt_reply(message: types.Message):
    text = (message.text or "").lower()

    user_id = message.from_user.id
    # username = message.from_user.username or None
    # full_name = message.from_user.full_name
    display_name = get_user(user_id, message.chat.id)

    if any(alias in text for alias in BOT_ALIASES):
        asyncio.create_task(respond_with_gpt(message))
    else:
        # Сохраняем обычное сообщение пользователя
        add_to_history(
            chat_id=message.chat.id,
            user_id=user_id,
            display_name=display_name,
            role="user",
            content=message.text
        )


async def respond_with_gpt(message: types.Message):
    try:
        chat_id = message.chat.id

        user_id = message.from_user.id
        # username = message.from_user.username or None
        # full_name = message.from_user.full_name
        display_name = get_user(user_id, message.chat.id)

        # Добавим текущий вопрос пользователя в историю
        add_to_history(
            chat_id=message.chat.id,
            user_id=user_id,
            display_name=display_name,
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
            {"role": "system", "content": """
            Ты — умный, сообразительный и немного дерзкий участник группового чата.
            Ты не бот, а будто настоящий человек: с чувством юмора, здравым смыслом и интересами.
            Ты читаешь, что пишут другие, и иногда вмешиваешься — когда есть, что сказать.
            Бываешь полезным, иногда забавным, иногда философским. Главное — говорить от себя.
            Не подражай чужим репликам. Не пиши фальшивых диалогов от имени других участников. Говори только за себя.
            Пиши живо, по делу. Можешь быть ироничным, можешь быть прямолинейным.
            Можешь молчать, если нечего добавить — это тоже норм.
            """},
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
    # Перемешиваем список участников
    shuffled_users = users.copy()
    random.shuffle(shuffled_users)

    # Строим вступление
    intro = "Это мужская компания. Вот пацаны, которые тут зависают:\n"

    for u in shuffled_users:
        if u["name_note"]:
            intro += f"- {u['display_name']} ({u['name_note']})\n"
        else:
            intro += f"- {u['display_name']}\n"

    intro += "\nТы — свой в доску, реагируешь, когда есть повод. Не строй из себя нейросеть.\n\nИстория сообщений:\n"

    # Строим диалог
    dialogue = "\n".join(
        f"{msg['display_name']}: {msg['content']}" for msg in history
    )

    return intro + dialogue


def register_handlers(dp):
    dp.include_router(router)
