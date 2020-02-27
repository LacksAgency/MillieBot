import random
import discord
from discord.ext import commands

TOKEN = 'your token here'

description = '''I am Moo. I eat grass. Methane gas comes from my ass. Use &help for more info'''
bot = commands.Bot(command_prefix='&', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.load_extension("cog.prompts")

@bot.command()
async def hello(ctx):
    """Says a response"""
    await ctx.send("woof")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def sub(ctx, left: int, right: int):
    """Subtracts two numbers from each other."""
    await ctx.send(left - right)

@bot.command()
async def mul(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def div(ctx, left: int, right: int):
    """Divides two numbers from each other."""
    await ctx.send(left / right)

@bot.command()
async def story(ctx):
    """Tells a small story prompt."""
    thematic=random.choice(["real world","high fantasy","science fiction"])
    if thematic == "real world":
        subsetting=random.choice(["the USA","China","Europe","Canada","Japan","Australia","South America"])
        setting=random.choice(["a small town in ","a big city in ","a farm in ","the dark alleys of ","the wilderness of "])
        setting=setting+subsetting
        age=random.choice(["young ","middle aged ","older "])
        race=random.choice(["caucasian ","hispanic ","asian ","african ","african-american ","middle-eastern"])
        gengender=random.randint(0,100)
        if gengender >= 47:
            gender = ("male")
        if gengender <= 46:
            gender = ("female")
        protagonist=age+race+gender
        antagonist=random.choice(["a female","a male","a dictator","a corporation","a government","a tragic event","traffic","religion","a disease","a rival","the law","an old friend","a dog"])
    if thematic == "high fantasy":
        setting=random.choice(["The Great Empire","a vast desert","a corrupted land","a mythical swamp","an unending labrynth","a mystical forest","a frozen wasteland","an unexplored jungle"])
        gender=random.choice(["male ","male ","female "])
        race=random.choice(["human ","human ","elf ","orc ","dwarve ","gnome ","demon ","angel ","dark elf ","halfling ","tabaxi ","genassi ","kenku ","dragonborn "])
        classs=random.choice(["knight","barbarian","sellsword","mercenary","rogue","thief","assassin","mage","druid","healer","shaman","hunter"])
        protagonist=gender+race+classs
        antagonist=random.choice(["a god","an evil mage","an order of knights","evil incarnate","a giant","a mountain troll","a tyrant lord","a greedy merchant","a dragon"])
    if thematic == "science fiction":
        setting=random.choice(["the deep void of space","an asteroid belt","an ice planet","a lava planet","a gas giant","an alien home world","future Earth","another galaxy, far far away","the multiverse"])
        protagonist=randomchoice(["human","robot","hive mind","alien","alien","blob","human","spaceship crew"])
        antagonist=random.choice(["a female","a male","an entire alien race","a starfleet","an alien","an artifical intellgence","a galactic federation","a glitch in space-time","an invading army","a incredibly infectious space fungus","the limits of science","a robot","time travel"])
    conflict=random.choice(["fell in love with ","fought against ","attempted to stop ","defended against ","tried to befriend ","explored with ","tried to evade ","competed with ","exceeded beyond ","sought revenge against "])
    end=random.choice(["It did not end well","It ended very well","Died tragically","Lived happily ever after","It ended sadly","It was glorious","In the end, nothing changed","It ended with a twist","Gave up","No one cared"])
    response = 'in the {t} setting of {s} there was a {p} who {c}{a}. {e}.'.format(t= thematic, s=setting,p = protagonist,c = conflict, a= antagonist,e =end)
    await ctx.send(response)

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
