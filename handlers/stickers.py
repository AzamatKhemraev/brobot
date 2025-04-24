from aiogram import Router, types
# from aiogram.filters import ChatTypeFilter

router = Router()


@router.message()
async def get_sticker_id(message: types.Message):
    # Проверяем: личный чат и стикер
    if message.chat.type == "private" and message.sticker:
        file_id = message.sticker.file_id
        emoji = message.sticker.emoji or "🤔"
        await message.reply(
            f"📎 File ID стикера: `{file_id}`\nЭмодзи: {emoji}",
            parse_mode="Markdown"
        )


def register_handlers(dp):
    dp.include_router(router)
