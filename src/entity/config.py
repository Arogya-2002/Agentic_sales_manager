from src.exceptions import CustomException
from src.logger import logging
from src.constants import *
import sys

class ConfigEntity:
    def __init__(self):
        try:
            self.agent_1_instruction = AGENT_1_INSTRUCTION
            self.agent_2_instruction = AGENT_2_INSTRUCTION
            self.agent_3_instruction = AGENT_3_INSTRUCTION
            self.sales_agent_picker_instruction = SALES_AGENT_PICKER_INSTRUCTION
            self.sales_manager_instruction = SALES_MANAGER_INSTRUCTION


            self.salesagent_name_1 = SALESAGENT_NAME_1
            self.salesagent_name_2 = SALESAGENT_NAME_2
            self.salesagent_name_3 = SALESAGENT_NAME_3
            self.salesagent_picker_name = SALESAGENT_PICKER_NAME
            self.sales_manager_name = SALES_MANAGER_NAME

            self.description = DESCRIPTION

            self.model = MODEL
            self.from_email = FROM_EMAIL
            self.to_email = TO_EMAIL
            self.email_tool_name = EMAIL_TOOL_NAME


            self.sendgrid_api_key = SENDGRID_API_KEY
            self.openai_api_key = OPENAI_API_KEY

        except Exception as e:
            raise CustomException(e,sys)

class AiAgentsConfig:
    def __init__(self,config:ConfigEntity):
        try:
            self.agent_1_instruction = config.agent_1_instruction
            self.agent_2_instruction = config.agent_2_instruction
            self.agent_3_instruction = config.agent_3_instruction
            self.sales_agent_picker_instruction = config.sales_agent_picker_instruction
            

            self.salesagent_name_1 = config.salesagent_name_1
            self.salesagent_name_2 = config.salesagent_name_2
            self.salesagent_name_3 = config.salesagent_name_3
            self.salesagent_picker_name = config.salesagent_picker_name
            



            self.model = config.model

        except Exception as e:
            raise CustomException(e,sys)
        

class AiToolsConfig:
    def __init__(self,config:ConfigEntity):
        try:
            self.from_email = config.from_email
            self.to_email = config.to_email
            self.email_tool_name = config.email_tool_name
            self.description = config.description
            self.sendgrid_api_key = config.sendgrid_api_key
            self.sales_manager_instruction = config.sales_manager_instruction
            self.sales_manager_name = config.sales_manager_name
            self.model = config.model
        except Exception as e:
            raise CustomException(e,sys)