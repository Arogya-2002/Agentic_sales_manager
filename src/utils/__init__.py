from typing import Dict
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
import asyncio
from agents import Agent, Runner, trace, function_tool

from src.exceptions import CustomException
from src.logger import logging
import sys
from src.constants import *

from typing import Optional
import uuid
import mysql.connector
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

from src.components.conversation import get_or_create_conversation, log_message

@function_tool
async def send_email(body: str, to_email: str = TO_EMAIL):
    """ Send out an email with the given body to a prospect and log it in MySQL """
    try:
        # 1️⃣ Create/Get Conversation
        conversation_id = get_or_create_conversation(to_email)

        # 2️⃣ Send Email
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        from_email = Email(FROM_EMAIL)
        to_email_obj = To(to_email)
        content = Content("text/plain", body)
        mail = Mail(from_email, to_email_obj, EMAIL_TOOL_NAME, content).get()
        sg.client.mail.send.post(request_body=mail)

        # 3️⃣ Log Message to MySQL
        message_id = log_message(conversation_id, "AI", body)

        return {"status": "success", "conversation_id": conversation_id, "message_id": message_id}

    except Exception as e:
        raise CustomException(e, sys)
