from database.db import DB_PATH
import aiosqlite


# Добавить пользователя в базу, если ещё не был
async def add_user(user_id: int, chat_id: int, username: str, full_name: str):
    db = await aiosqlite.connect(DB_PATH)
    await db.execute(
        """
        INSERT OR IGNORE INTO users (user_id, chat_id, username, full_name)
        VALUES (?, ?, ?, ?)
        """,
        (user_id, chat_id, username, full_name)
    )
    await db.commit()
    await db.close()


# Получить всех пользователей из одного чата
async def get_users_by_chat(chat_id: int):
    db = await aiosqlite.connect(DB_PATH)
    cursor = await db.execute(
        "SELECT * FROM users WHERE chat_id = ?",
        (chat_id,)
    )
    rows = await cursor.fetchall()
    await db.close()
    return rows


# Получить одного пользователя
async def get_user(user_id: int, chat_id: int):
    db = await aiosqlite.connect(DB_PATH)
    cursor = await db.execute(
        "SELECT * FROM users WHERE user_id = ? AND chat_id = ?",
        (user_id, chat_id)
    )
    user = await cursor.fetchone()
    await db.close()
    return user
