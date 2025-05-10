from aiogram import Dispatcher
from . import history, echo, mention, stickers, scan


def register_handlers(dp: Dispatcher):
    history.register_handlers(dp)
    echo.register_handlers(dp)
    mention.register_handlers(dp)
    stickers.register_handlers(dp)
    scan.register_handlers(dp)
