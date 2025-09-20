# src/pipeline/followup.py
import mysql.connector
from src.components.conversation import get_connection
from src.components.conversation_agent import ConversationAgent
from src.utils import send_email

async def handle_followup(conversation_id: str, to_email: str):
    """
    Loads conversation history, runs the ConversationAgent, and sends a follow-up email.
    """
    # 1️⃣ Fetch conversation history
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT sender, content FROM messages 
        WHERE conversation_id=%s ORDER BY created_at ASC
    """, (conversation_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    conversation_history = "\n".join([f"{row['sender']}: {row['content']}" for row in rows])

    # 2️⃣ Run ConversationAgent
    agent = ConversationAgent(model="gpt-4o-mini", tools=[])
    reply = await agent.handle_reply(conversation_history, rows[-1]['content'])

    # 3️⃣ Send email + log automatically
    await send_email(reply, to_email=to_email)
