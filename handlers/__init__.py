from aiogram import Dispatcher
from . import scan, history, echo, mention, stickers


def register_handlers(dp: Dispatcher):
    scan.register_handlers(dp)
    history.register_handlers(dp)
    echo.register_handlers(dp)
    mention.register_handlers(dp)
    stickers.register_handlers(dp)
