from src.components.aiagents import AiAgents
from src.components.aitools import AiTools
from src.logger import logging
import asyncio

async def main():
    try:
        logging.info("Starting the agent pipeline")
        ai_agents = AiAgents()
        agents_list = ai_agents.initialize_agents().agents_list

        ai_tools = AiTools()
        tools_list = ai_tools.initiate_tools(agents_list)
        
        # Await the asynchronous function call
        result = await ai_tools.planning_agent(tools_list)
        
        print("Pipeline execution complete.")
        print(f"Final Result: {result}")
        logging.info("Agent pipeline finished successfully.")
    except Exception as e:
        logging.error(f"An error occurred in the pipeline: {e}")

if __name__ == "__main__":
    asyncio.run(main())