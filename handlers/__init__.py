from aiogram import Dispatcher
from . import echo, mention, stickers, chat_observer


def register_handlers(dp: Dispatcher):
    echo.register_handlers(dp)
    mention.register_handlers(dp)
    stickers.register_handlers(dp)
    chat_observer.register_handlers(dp)
