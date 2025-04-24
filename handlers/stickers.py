from aiogram import Router, types

router = Router()


@router.message()
async def get_sticker_id(message: types.Message):
    print("👀 Сообщение пришло:", message.chat.type)

    if message.chat.type == "private" and message.sticker:
        file_id = message.sticker.file_id
        emoji = message.sticker.emoji or "🤔"

        print("📦 Получен стикер:", file_id)

        await message.reply(
            f"📎 File ID стикера: `{file_id}`\nЭмодзи: {emoji}",
            parse_mode="Markdown"
        )


def register_handlers(dp):
    dp.include_router(router)
