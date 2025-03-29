import discord
from discord.ext import commands
import ollama
import os
import dotenv
import asyncio
import pyjokes
import random  
import re  

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise ValueError("❌ Missing Discord Bot Token in environment variables.")

# Set up Discord bot with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
# Remove default help command to avoid conflicts
bot.remove_command("help")

def clean_response(text):
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()  # Remove <think> tags
    return text[:4000]  

async def get_ai_response(prompt):
    try:
        response = await asyncio.to_thread(
            ollama.chat, 
            model="deepseek-r1:8b",  
            messages=[{"role": "user", "content": prompt}],
            options={"num_predict": 200}  
        )
        return clean_response(response['message']['content'])
    except Exception as e:
        return f"❌ Error: {str(e)}"

async def send_long_message(channel, text):
    for i in range(0, len(text), 2000):
        await channel.send(text[i:i+2000])

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:  # Respond only when bot is mentioned
        prompt = message.content.replace(f"<@{bot.user.id}>", "").strip()
        if prompt:
            async with message.channel.typing():
                response = await get_ai_response(prompt)
            await send_long_message(message.channel, response)  

    await bot.process_commands(message)  

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(bot.latency * 1000)}ms")

# Coin flip command
@bot.command()
async def flip(ctx):
    result = "Heads" if random.randint(0,1) == 0 else "Tails"
    await ctx.send(f"🪙 {result}!")

# Joke command
@bot.command()
async def joke(ctx):
    joke = pyjokes.get_joke()
    await ctx.send(f"😄 {joke}")

# AI Chat command 
@bot.command()
async def ask(ctx, *, question: str):
    async with ctx.typing():
        response = await get_ai_response(question)
    await send_long_message(ctx.channel, response)  

# Custom Help Command (renamed from "help" to "commands")
@bot.command(name="commands")
async def custom_help(ctx):
    """Displays a list of bot commands."""
    embed = discord.Embed(
        title="🤖 Bot Commands",
        description="Here are the available commands:",
        color=discord.Color.blurple()
    )
    embed.add_field(name="🏓 !ping", value="Check bot latency", inline=False)
    embed.add_field(name="🪙 !flip", value="Flip a coin", inline=False)
    embed.add_field(name="😄 !joke", value="Get a random joke", inline=False)
    embed.add_field(name="💬 !ask [question]", value="Ask AI a question", inline=False)
    embed.add_field(name="📜 !commands", value="Show this help message", inline=False)
    await ctx.send(embed=embed)

# Run the bot
bot.run(TOKEN)
