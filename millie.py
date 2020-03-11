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
    woof=random.choice(["woof", "bark", "*whines happily*", "*wags tail*", "*wags whole butt out of excitement*", "*starts trying to lick you while still 3 feet away*"])
    resp = '{response}'.format(response= woof)
    print('hello')
    print(resp)
    print('-----')
    await ctx.send(resp)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    print('roll')
    print(dice)
    print(rolls)
    print('-----')
    await ctx.send(result)

@bot.command()
async def guess(ctx, g : int):
    """Guess a number between 1 and 5"""
    num = random.randint(1, 5)
    if g == num:
        print ('Guess = Correct')
        print ('-----')
        await ctx.send('Correct!')
    else:
        print ('Guess = Wrong. Num is ', num)
        print ('-----')
        await ctx.send("I'm sorry, that is incorrect.")

bot.run(TOKEN)
