import random
import discord
from discord.ext import commands

TOKEN = 'Your Token'

description = '''I am Moo. I eat grass. Methane gas comes from my ass. Use &help for more info'''
bot = commands.Bot(command_prefix='&', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.load_extension("cog.prompts")
    bot.load_extension("cog.story")
    bot.load_extension("cog.math")
    
@bot.command()
async def hello(ctx):
    """Says a response"""
    await ctx.send("woof")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

bot.run(TOKEN)
