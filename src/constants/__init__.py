from dotenv import load_dotenv
import os

AGENT_1_INSTRUCTION= "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

AGENT_2_INSTRUCTION = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

AGENT_3_INSTRUCTION = "You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."

SALES_AGENT_PICKER_INSTRUCTION =" You pick the best cold sales email from the given options. \
Imagine you are a customer and pick the one you are most likely to respond to. \
Do not give an explanation; reply with the selected email only."


DESCRIPTION = "Write a cold sales email"


SALES_MANAGER_INSTRUCTION = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the sales_agent tools.
 
Follow these steps carefully:
1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.
 
2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.
 
3. Use the send_email tool to send the best email (and only the best email) to the user.
 
Crucial Rules:
- You must use the sales agent tools to generate the drafts — do not write them yourself.
- You must send ONE email using the send_email tool — never more than one.
"""



SALESAGENT_NAME_1 = "Professional Sales Agent"
SALESAGENT_NAME_2 = "Engaging Sales Agent"
SALESAGENT_NAME_3 = "Busy Sales Agent"
SALESAGENT_PICKER_NAME = "Sales_picker"
SALES_MANAGER_NAME = "Sales Manager"


MODEL = "gpt-4o-mini"


FROM_EMAIL =   "arogyavamshi.chinnabathini@tekworks.in"
TO_EMAIL = "arogyavamshi2002@gmail.com"
EMAIL_TOOL_NAME = "Sales email"


load_dotenv()
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")