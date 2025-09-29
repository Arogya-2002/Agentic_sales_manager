import asyncio
from src.components.aiagents import AiAgents
from src.components.aitools import AiTools
from src.logger import logging
from src.entity.config import ConfigEntity

async def run_outreach_campaign():
    """
    Initializes and runs the cold email outreach pipeline for a specific prospect.
    """
    try:
        logging.info("Starting new outreach campaign...")
        # 1. Initialize Agents
        ai_agents_obj = AiAgents()
        agents_artifact = ai_agents_obj.initialize_agents()
        agents_list = agents_artifact.agents_list
        logging.info(f"Initialized {len(agents_list)} agents.")

        # 2. Initialize Tools
        ai_tools_obj = AiTools()
        tools = ai_tools_obj.initiate_tools(agents_list)
        logging.info(f"Initialized {len(tools)} tools.")

        # 3. Define the outreach prompt and target
        config = ConfigEntity()
        prospect_name = "Vamshi"
        prospect_email = config.to_email  # Using the email from config
        
        prompt = (f"Your task is to send a compelling cold sales email to a prospect named '{prospect_name}' "
                  f"at the email address '{prospect_email}'. The email should introduce our company, 'ComplAI', "
                  "and its AI-powered SaaS tool for SOC2 compliance and audits.")

        # 4. Run the planning agent
        logging.info("Executing the Sales Manager agent to orchestrate the campaign...")
        result = await ai_tools_obj.planning_agent(tools, prompt)
        
        logging.info("Outreach campaign finished.")
        print("--- Campaign Result ---")
        print(result)
        print("-----------------------")

    except Exception as e:
        logging.error(f"An error occurred during the outreach campaign: {e}")

if __name__ == "__main__":
    asyncio.run(run_outreach_campaign())