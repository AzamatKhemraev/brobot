from aiogram import Router, types
from aiogram.filters import Command
from services.gif_search import get_random_gif_url

router = Router()


@router.message(Command("gif"))
async def send_random_gif(message: types.Message):

    await message.bot.send_chat_action(message.chat.id, "choose_sticker")

    gif_url = await get_random_gif_url()

    if gif_url:
        await message.reply_animation(gif_url)
    else:
        await message.reply("🙁 Не удалось найти случайную гифку. Попробуй ещё раз!")


def register_handlers(dp):
    dp.include_router(router)
