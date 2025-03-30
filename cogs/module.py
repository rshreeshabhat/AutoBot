from discord.ext import commands
import random
import pyjokes
import discord

class Module(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Check bot latency."""
        await ctx.send(f"🏓 Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def flip(self, ctx):
        """Flip a coin."""
        result = "Heads" if random.randint(0, 1) == 0 else "Tails"
        await ctx.send(f"🪙 {result}!")

    @commands.command()
    async def joke(self, ctx):
        """Get a random joke."""
        joke = pyjokes.get_joke()
        await ctx.send(f"😄 {joke}")

    @commands.command(name="commands")
    async def custom_help(self, ctx):
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

async def setup(bot):
    """Load Module cog asynchronously."""
    await bot.add_cog(Module(bot))  # ✅ Awaited correctly
