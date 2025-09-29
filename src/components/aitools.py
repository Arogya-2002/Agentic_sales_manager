from src.exceptions import CustomException
from src.logger import logging
import sys
from src.entity.config import ConfigEntity,AiToolsConfig
from agents import Agent, Runner, trace
from src.utils import send_email

class AiTools:
    def __init__(self):
        self.ai_tools_config = AiToolsConfig(config=ConfigEntity())

    def initiate_tools(self,agents_list):
        try:
            tool1 = agents_list[0].as_tool(tool_name="sales_agent1", tool_description=self.ai_tools_config.description)
            tool2 = agents_list[1].as_tool(tool_name="sales_agent2", tool_description=self.ai_tools_config.description)
            tool3 = agents_list[2].as_tool(tool_name="sales_agent3", tool_description=self.ai_tools_config.description)
            
            # NEW: Creating a tool for the picker agent
            picker_tool = agents_list[3].as_tool(
                tool_name=self.ai_tools_config.sales_picker_tool_name, 
                tool_description=self.ai_tools_config.sales_picker_tool_description
            )

            tools = [tool1, tool2, tool3, picker_tool, send_email]
            return tools
        except Exception as e:
            raise CustomException(e,sys)
        
    # MODIFIED: Function now accepts a dynamic 'outreach_prompt'
    async def planning_agent(self, tools, outreach_prompt: str):
        try:
            sales_manager = Agent(
                name=self.ai_tools_config.sales_manager_name,
                instructions=self.ai_tools_config.sales_manager_instruction,
                tools=tools,
                model=self.ai_tools_config.model
            )

            logging.info(f"Running sales manager with prompt: {outreach_prompt}")
            with trace("Sales manager"):
                result = await Runner.run(sales_manager, outreach_prompt)

            return result
        except Exception as e:
            raise CustomException(e, sys)