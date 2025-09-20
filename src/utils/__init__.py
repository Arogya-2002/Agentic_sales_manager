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


@function_tool
async def send_email(body: str):
    """ Send out an email with the given body to all sales prospects """
    try:
        
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        from_email = Email(FROM_EMAIL)
        to_email = To(TO_EMAIL)
        content = Content("text/plain", body)
        mail = Mail(from_email, to_email, EMAIL_TOOL_NAME, content).get()
        sg.client.mail.send.post(request_body=mail)
        return {"status": "success"}
    except Exception as e:
        raise CustomException(e,sys)