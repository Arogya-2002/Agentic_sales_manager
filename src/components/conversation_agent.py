# src/components/conversation_agent.py
from agents import Agent, Runner, trace

class ConversationAgent:
    def __init__(self, model, tools):
        self.agent = Agent(
            name="Conversation Agent",
            model=model,
            tools=tools,
            instructions="""
You are an AI sales assistant. You are continuing an email conversation with a prospect.
Analyze the full conversation history and generate an appropriate response.
- If they are interested, move them closer to booking a call/demo.
- If they object, handle objections politely and try to re-engage.
- If they clearly say "no" or "stop", politely thank them and end the conversation.
Keep replies short and professional.
"""
        )

    async def handle_reply(self, conversation_history, last_message):
        prompt = f"""
Conversation so far:
{conversation_history}

Latest message from prospect:
{last_message}

Write your next email response.
"""
        with trace("Conversation agent"):
            return await Runner.run(self.agent, prompt)
