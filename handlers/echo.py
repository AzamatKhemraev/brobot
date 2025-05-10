from aiogram import Router, types
from aiogram.filters import Command

# Создаём роутер
router = Router()


# Обработка команды /echo
@router.message(Command("echo"))
async def echo_cmd(message: types.Message):
    await message.reply("Дич сук")

    print('asdad')


# Функция для регистрации хендлеров
def register_handlers(dp):
    dp.include_router(router)
