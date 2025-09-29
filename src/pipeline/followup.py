from src.components.conversation import get_db_pool  # MODIFIED: Using async pool
from src.components.conversation_agent import ConversationAgent
from src.utils import send_email
import aiomysql

# MODIFIED: Function is now fully async with async DB calls
async def handle_followup(conversation_id: str, to_email: str):
    """
    Loads conversation history, runs the ConversationAgent, and sends a follow-up email.
    """
    # 1️⃣ Fetch conversation history
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("""
                SELECT sender, content FROM messages 
                WHERE conversation_id=%s ORDER BY created_at ASC
            """, (conversation_id,))
            rows = await cursor.fetchall()

    conversation_history = "\n".join([f"{row['sender']}: {row['content']}" for row in rows])

    # 2️⃣ Run ConversationAgent
    agent = ConversationAgent(model="gpt-4o-mini", tools=[])
    reply_content = await agent.handle_reply(conversation_history, rows[-1]['content'])

    # 3️⃣ Send email (which also logs the AI message)
    await send_email(reply_content, to_email=to_email)