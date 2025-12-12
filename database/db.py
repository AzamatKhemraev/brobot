import aiosqlite
import os

# Путь к базе — по умолчанию файл создаётся рядом с проектом
DB_PATH = os.getenv("DB_PATH", "brobot.db")


# Получаем подключение
async def get_db():
    return await aiosqlite.connect(DB_PATH)


# Инициализация таблиц
async def init_db():
    db = await aiosqlite.connect(DB_PATH)
    await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            chat_id INTEGER NOT NULL,
            chat_type TEXT,
            username TEXT,
            full_name TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            display_name TEXT,
            name_note TEXT,
            UNIQUE(user_id, chat_id)
        );
    """)
    await db.commit()
    await db.close()
