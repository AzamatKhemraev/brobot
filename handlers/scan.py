from aiogram import Router, types
from aiogram.filters import Command
from database.user_service import add_user

router = Router()

AUTHORIZED_USERNAME = "azamat_khemraev"  # без @


@router.message(Command("scan"))
async def scan_command(message: types.Message):
    sender = message.from_user

    if sender.username != AUTHORIZED_USERNAME:
        await message.reply("🚫 У тебя нет доступа к этой команде.")
        return

    await add_user(
        user_id=sender.id,
        chat_id=message.chat.id,
        username=sender.username or "",
        full_name=sender.full_name
    )

    await message.reply("✅ Ты добавлен в базу (или уже был).")


def register_handlers(dp):
    dp.include_router(router)
