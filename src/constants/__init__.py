from dotenv import load_dotenv
import os

load_dotenv()

AGENT_1_INSTRUCTION= "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

AGENT_2_INSTRUCTION = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

AGENT_3_INSTRUCTION = "You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."

SALES_AGENT_PICKER_INSTRUCTION ="You are an expert at picking the best cold sales email from a list of options. \
Imagine you are a customer and pick the one you are most likely to respond to. \
Do not give an explanation; reply with the selected email only."

DESCRIPTION = "Write a cold sales email"
SALES_PICKER_TOOL_DESCRIPTION = "Selects the single best email from a list of provided email drafts."

# MODIFIED: Updated instructions for the manager to use the picker tool.
SALES_MANAGER_INSTRUCTION = """
You are a Sales Manager at ComplAI. Your goal is to find and send the single best cold sales email.
 
Follow these steps carefully:
1. Generate Drafts: Use the `sales_agent1`, `sales_agent2`, and `sales_agent3` tools to generate three different email drafts based on the user's request.
 
2. Evaluate and Select: Use the `sales_email_picker` tool. Provide it with the three generated drafts to choose the single best one.
 
3. Send the Email: Use the `send_email` tool to send ONLY the final selected email to the prospect.
 
Crucial Rules:
- You must use the sales agent tools to generate the drafts — do not write them yourself.
- You must use the sales_email_picker tool to select the final draft.
- You must send ONLY ONE email using the `send_email` tool.
"""

SALESAGENT_NAME_1 = "Professional Sales Agent"
SALESAGENT_NAME_2 = "Engaging Sales Agent"
SALESAGENT_NAME_3 = "Busy Sales Agent"
SALESAGENT_PICKER_NAME = "Sales_picker"
SALES_MANAGER_NAME = "Sales Manager"
SALES_PICKER_TOOL_NAME = "sales_email_picker"

MODEL = "gpt-4o-mini"

FROM_EMAIL = "arogyavamshi.chinnabathini@tekworks.in"
TO_EMAIL = "arogyavamshi2002@gmail.com"
EMAIL_TOOL_NAME = "Sales email"

# API Keys
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# NEW: Database credentials from .env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")