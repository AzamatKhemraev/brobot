from aiogram import Dispatcher
from . import echo, mention, stickers, history


def register_handlers(dp: Dispatcher):
    echo.register_handlers(dp)
    mention.register_handlers(dp)
    stickers.register_handlers(dp)
    history.register_handlers(dp)
