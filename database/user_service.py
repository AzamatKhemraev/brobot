from database.db import get_db


async def add_user(user_id: int, chat_id: int, username: str, full_name: str):
    async with await get_db() as db:
        await db.execute(
            """
            INSERT OR IGNORE INTO users (user_id, chat_id, username, full_name)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, chat_id, username, full_name)
        )
        await db.commit()


async def get_users_by_chat(chat_id: int):
    async with await get_db() as db:
        cursor = await db.execute(
            "SELECT * FROM users WHERE chat_id = ?",
            (chat_id,)
        )
        return await cursor.fetchall()


async def get_user(user_id: int, chat_id: int):
    async with await get_db() as db:
        cursor = await db.execute(
            "SELECT * FROM users WHERE user_id = ? AND chat_id = ?",
            (user_id, chat_id)
        )
        return await cursor.fetchone()
