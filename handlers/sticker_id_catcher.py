from aiogram import Router, types

router = Router()


@router.message(lambda m: m.sticker is not None)
async def catch_sticker(message: types.Message):
    file_id = message.sticker.file_id
    emoji = message.sticker.emoji or "🤔"

    await message.reply(f"🆔 Стикер ID:\n`{file_id}`\n\n{emoji}", parse_mode="Markdown")
    print(f"[DEBUG] Стикер: {file_id} (emoji: {emoji})")


# Функция для регистрации хендлеров
def register_handlers(dp):
    dp.include_router(router)
