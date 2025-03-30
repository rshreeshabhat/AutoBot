from discord.ext import commands
import asyncio
import ollama
import re

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_ai_response(self, prompt):
        """Fetch AI response from Ollama."""
        try:
            response = await asyncio.to_thread(
                ollama.chat, 
                model="deepseek-r1:8b",  
                messages=[{"role": "user", "content": prompt}],
                options={"num_predict": 200}  
            )
            return re.sub(r"<think>.*?</think>", "", response['message']['content']).strip()
        except Exception as e:
            return f"❌ Error: {str(e)}"

@commands.command()
async def ask(self, ctx, *, question: str):
    """Ask the AI a question."""
    async with ctx.typing():
        response = await self.get_ai_response(question)
    await ctx.send(response)

async def setup(bot):
    """Load AI cog asynchronously."""
    await bot.add_cog(AI(bot))  # ✅ Now we await it
