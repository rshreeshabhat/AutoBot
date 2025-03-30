import discord
from discord.ext import commands
import os
import asyncio
from utils import config

# Bot setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

async def load_cogs():
    """Loads all cogs dynamically."""
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"✅ Loaded {filename}")
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(config.TOKEN)

# Run the bot with asyncio
asyncio.run(main())
