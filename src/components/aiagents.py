from src.exceptions import CustomException
from src.logger import logging

from src.entity.config import ConfigEntity,AiAgentsConfig
from src.entity.artifact import AiAgentsArtifact
from agents import Agent, Runner, trace, function_tool
from openai.types.responses import ResponseTextDeltaEvent



import sys

class AiAgents:
    def __init__(self):
        self.ai_agents_config = AiAgentsConfig(config=ConfigEntity())
    
    def initialize_agents(self):
        try:
            logging.info("Initializing agents")
            sales_agent1 = Agent(
                name="Professional Sales Agent",
                instructions= self.ai_agents_config.agent_1_instruction,
                model=self.ai_agents_config.model)

            sales_agent2 = Agent(
                    name="Engaging Sales Agent",
                    instructions=self.ai_agents_config.agent_2_instruction,
                    model=self.ai_agents_config.model)

            sales_agent3 = Agent(
                    name="Busy Sales Agent",
                    instructions=self.ai_agents_config.agent_3_instruction,
                    model=self.ai_agents_config.model)
            

            sales_picker = Agent(
                name = self.ai_agents_config.salesagent_picker_name,
                instructions = self.ai_agents_config.sales_agent_picker_instruction,
                model = self.ai_agents_config.model
            )


            return AiAgentsArtifact(agents_list=[sales_agent1,sales_agent2,sales_agent3,sales_picker]) #sales_agent1,sales_agent2,sales_agent3,sales_picker
        except Exception as e:
            raise CustomException(e,sys)    
        