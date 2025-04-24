from aiogram import Router, types

router = Router()


@router.message()
async def debug_any_message(message: types.Message):
    print("🔥 БОТ ПОЛУЧИЛ СООБЩЕНИЕ!")
    print("➡️ Тип:", message.content_type)

    if message.sticker:
        print("🎯 Это стикер!")
        await message.reply(f"🧷 file_id: `{message.sticker.file_id}`", parse_mode="Markdown")
    else:
        await message.reply("📭 Это не стикер.")


def register_handlers(dp):
    dp.include_router(router)
