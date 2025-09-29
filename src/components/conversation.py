import aiomysql  # MODIFIED: Using async library
import uuid
from src.entity.config import ConfigEntity, DbConfig

# Global pool variable
db_pool = None

# NEW: Asynchronous function to initialize the database connection pool
async def get_db_pool():
    global db_pool
    if db_pool is None:
        db_config = DbConfig(config=ConfigEntity())
        db_pool = await aiomysql.create_pool(
            host=db_config.host,
            user=db_config.user,
            password=db_config.password,
            db=db_config.db,
            autocommit=True
        )
    return db_pool

# MODIFIED: All database functions are now async
async def get_or_create_conversation(prospect_email: str):
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM conversations WHERE prospect_email=%s", (prospect_email,))
            existing = await cursor.fetchone()
            if existing:
                return existing["id"]

            conversation_id = str(uuid.uuid4())
            await cursor.execute("""
                INSERT INTO conversations (id, prospect_email, status, next_action)
                VALUES (%s, %s, 'in_progress', 'WAITING_REPLY')
            """, (conversation_id, prospect_email))
            return conversation_id

async def log_message(conversation_id: str, sender: str, content: str):
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            message_id = str(uuid.uuid4())
            await cursor.execute("""
                INSERT INTO messages (id, conversation_id, sender, content)
                VALUES (%s, %s, %s, %s)
            """, (message_id, conversation_id, sender, content))

            await cursor.execute("""
                UPDATE conversations
                SET last_message_by=%s, last_message_content=%s, updated_at=NOW()
                WHERE id=%s
            """, (sender, content, conversation_id))
            return message_id