# webhook.py
from fastapi import FastAPI, Request, Form
from src.components.conversation import get_or_create_conversation, log_message
from src.pipeline.followup import handle_followup
from src.exceptions import CustomException
from src.logger import logging
import sys

app = FastAPI()

@app.post("/email-reply")
async def email_reply(request: Request):
    """
    Handles inbound email replies from SendGrid's Inbound Parse Webhook.
    """
    try:
        form_data = await request.form()
        from_email = form_data.get("from")
        subject = form_data.get("subject")
        body = form_data.get("text")  # plain text email body

        logging.info(f"Received reply from {from_email}: {body}")

        # 1️⃣ Find or create a conversation
        conversation_id = get_or_create_conversation(from_email)

        # 2️⃣ Log prospect message
        log_message(conversation_id, "PROSPECT", body)

        # 3️⃣ Trigger AI follow-up
        await handle_followup(conversation_id, from_email)

        return {"status": "ok"}

    except Exception as e:
        raise CustomException(e, sys)
