import asyncpg

from config import settings

async def connect_to_postgresql():
    connection = await asyncpg.connect(
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        database=settings.POSTGRES_DB,
        host=settings.POSTGRES_HOST
    )
    return connection

async def add_chat_to_user(login, chat_id):
    connection = await connect_to_postgresql()
    query = 'UPDATE users SET chat_id = $1 WHERE login = $2'
    try:
        await connection.execute(query, chat_id, login)
    finally:
        await connection.close()