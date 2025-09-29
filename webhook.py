from fastapi import FastAPI, Request
from src.components.conversation import get_or_create_conversation, log_message
from src.pipeline.followup import handle_followup
from src.exceptions import CustomException
from src.logger import logging
import sys

app = FastAPI()

# MODIFIED: Endpoint now calls async functions with 'await'
@app.post("/email-reply")
async def email_reply(request: Request):
    """
    Handles inbound email replies from SendGrid's Inbound Parse Webhook.
    """
    try:
        form_data = await request.form()
        from_email = form_data.get("from")
        # You may need to parse the from_email string as it can be "Name <email@example.com>"
        if '<' in from_email and '>' in from_email:
            from_email = from_email.split('<')[1].split('>')[0]
        
        body = form_data.get("text")

        logging.info(f"Received reply from {from_email}: {body}")

        # 1️⃣ Find or create a conversation
        conversation_id = await get_or_create_conversation(from_email)

        # 2️⃣ Log prospect message
        await log_message(conversation_id, "PROSPECT", body)

        # 3️⃣ Trigger AI follow-up
        await handle_followup(conversation_id, from_email)

        return {"status": "ok"}

    except Exception as e:
        # Note: Proper error handling in a production webhook is critical.
        # You might want to return a specific HTTP status code.
        logging.error(f"Error in webhook: {e}")
        # Re-raising might not be ideal, depends on FastAPI error handling setup
        raise CustomException(e, sys)