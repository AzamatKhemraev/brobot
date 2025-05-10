from aiogram import Dispatcher
from . import history, echo, mention, stickers


def register_handlers(dp: Dispatcher):
    history.register_handlers(dp)
    echo.register_handlers(dp)
    mention.register_handlers(dp)
    stickers.register_handlers(dp)
