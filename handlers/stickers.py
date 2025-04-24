from aiogram import Router, types

router = Router()


@router.message()
async def get_sticker_id(message: types.Message):
    # Проверка: сообщение в ЛС и содержит стикер
    if message.chat.type == "private" and message.sticker:
        file_id = message.sticker.file_id
        emoji = message.sticker.emoji or "🤔"
        await message.reply(
            f"📎 File ID стикера: `{file_id}`\nЭмодзи: {emoji}",
            parse_mode="Markdown"
        )


def register_handlers(dp):
    dp.include_router(router)
