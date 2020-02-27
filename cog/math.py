import discord
from discord.ext import commands

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together"""
    await ctx.send(left + right)

@commands.command()
async def sub(ctx, left: int, right: int):
    """Subtracts two numbers from each other"""
    await ctx.send(left - right)

@commands.command()
async def mul(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)

@commands.command()
async def div(ctx, left: int, right: int):
    """Divides two numbers from each other."""
    await ctx.send(left / right)

def setup(bot):
    bot.add_command(add)
    bot.add_command(sub)
    bot.add_command(mul)
    bot.add_command(div)
    bot.add_cog(Math(bot))