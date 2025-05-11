from aiogram import Router, types
from aiogram.filters import Command
from database.user_service import add_user

router = Router()


@router.message(Command("scan"))
async def scan_command(message: types.Message):
    sender = message.from_user

    await add_user(
        user_id=sender.id,
        chat_id=message.chat.id,
        chat_type=message.chat.type,
        username=sender.username or "",
        full_name=sender.full_name
    )

    await message.reply("✅ Ты добавлен в базу (или уже был).")


def register_handlers(dp):
    dp.include_router(router)
