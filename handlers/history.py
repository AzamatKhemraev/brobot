from aiogram import Router, types
from aiogram.filters import Command
from services.context import get_history, message_history

router = Router()


@router.message(Command("history"))
async def history_command(message: types.Message):
    chat_id = message.chat.id
    history = get_history(chat_id)

    if not history:
        await message.reply("¯\\(°_o)/¯ История сообщений пуста.")
        return

    # Форматируем историю
    formatted = []
    for i, entry in enumerate(history[-20:], 1):  # выводим только последние 20 сообщений
        role = "👤" if entry["role"] == "user" else "🤖"
        content = entry["content"].strip()
        if not content:
            continue
        formatted.append(f"{i}. {role} {content}")

    response = "\n\n".join(formatted)

    # Ограничение телеги: 4096 символов
    if len(response) > 4000:
        response = response[:500] + "\n\n... (обрезано)"

    await message.reply(response)


@router.message(Command("forget"))
async def forget_command(message: types.Message):
    chat_id = message.chat.id

    if chat_id in message_history:
        message_history[chat_id].clear()
        await message.reply("История чата очищена.")
    else:
        await message.reply("¯\\(°_o)/¯ История сообщений пуста.")


# Функция для регистрации хендлеров
def register_handlers(dp):
    dp.include_router(router)
