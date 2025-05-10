from aiogram import Dispatcher
from . import echo, mention, stickers


def register_handlers(dp: Dispatcher):
    echo.register_handlers(dp)
    mention.register_handlers(dp)
    stickers.register_handlers(dp)
