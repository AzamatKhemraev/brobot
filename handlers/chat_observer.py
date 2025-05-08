from aiogram import Router, types
from collections import deque
import datetime
# import asyncio

from services.gpt import chat_with_gpt

router = Router()

# История сообщений по чату
chat_activity = {}  # chat_id: deque[(text, timestamp)]

# Ограничения
MAX_MESSAGES = 5
TIME_WINDOW = 60  # секунд
COOLDOWN = 600    # бот не будет писать чаще, чем 1 раз в 10 мин

last_bot_reply = {}  # chat_id: datetime


@router.message()
async def watch_chat(message: types.Message):
    # Только групповые чаты
    if message.chat.type not in ["group", "supergroup"]:
        return

    chat_id = message.chat.id
    now = datetime.datetime.utcnow()

    # Инициализация очереди сообщений
    if chat_id not in chat_activity:
        chat_activity[chat_id] = deque(maxlen=MAX_MESSAGES)

    chat_activity[chat_id].append((message.text or "", now))

    # Проверка на количество сообщений и интервал
    messages = chat_activity[chat_id]
    if len(messages) < MAX_MESSAGES:
        return

    first_time = messages[0][1]
    last_time = messages[-1][1]
    delta = (last_time - first_time).total_seconds()

    if delta > TIME_WINDOW:
        return

    # Проверка на cooldown
    if chat_id in last_bot_reply:
        since_last = (now - last_bot_reply[chat_id]).total_seconds()
        if since_last < COOLDOWN:
            return

    # Генерация контекста и вызов GPT
    await message.bot.send_chat_action(chat_id, "typing")

    context = "\n".join([f"- {text}" for text, _ in messages if text])
    prompt = f"Ты наблюдаешь диалог в чате. Ответь в тему, дружелюбно или с юмором.\nВот что обсуждают:\n{context}"

    gpt_response = await chat_with_gpt(prompt)

    await message.answer(gpt_response)
    last_bot_reply[chat_id] = now


# Функция для регистрации хендлеров
def register_handlers(dp):
    dp.include_router(router)
