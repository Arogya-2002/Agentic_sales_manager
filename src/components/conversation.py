# src/database/conversation.py
import mysql.connector
import uuid
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="adminroot",
        database="sys"
    )

def get_or_create_conversation(prospect_email: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Try to find an existing conversation
    cursor.execute("SELECT * FROM conversations WHERE prospect_email=%s", (prospect_email,))
    existing = cursor.fetchone()

    if existing:
        cursor.close()
        conn.close()
        return existing["id"]

    # Create a new conversation if not found
    conversation_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO conversations (id, prospect_email, status, next_action)
        VALUES (%s, %s, 'in_progress', 'WAITING_REPLY')
    """, (conversation_id, prospect_email))
    conn.commit()
    cursor.close()
    conn.close()

    return conversation_id

def log_message(conversation_id: str, sender: str, content: str):
    conn = get_connection()
    cursor = conn.cursor()

    message_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO messages (id, conversation_id, sender, content)
        VALUES (%s, %s, %s, %s)
    """, (message_id, conversation_id, sender, content))

    cursor.execute("""
        UPDATE conversations
        SET last_message_by=%s, last_message_content=%s, updated_at=NOW()
        WHERE id=%s
    """, (sender, content, conversation_id))

    conn.commit()
    cursor.close()
    conn.close()
    return message_id
