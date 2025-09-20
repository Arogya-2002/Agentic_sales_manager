import mysql.connector
import uuid

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="adminroot",
        database="sys"
    )

def save_message(conversation_id, sender, content):
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
