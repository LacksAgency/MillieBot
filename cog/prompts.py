import discord
import random
from discord.ext import commands

class Prompts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def prompt(ctx):
    """Asks for a random tidbit of information about the world you are building"""
    genre=random.choice(["physics / nature","geography / natural resources","magic / religion","population","language / gestures","culture","celebrations","education","family","trade","conflict","governance","foods and drink"])
    if genre == "physics / nature":
        prompt=random.choice(["Are the laws of nature or physics different to earth? Elaborate.","Are there multiple suns or moons?","What does the sky look like during the day?","Describe a typical night sky and an extraordinary night sky.","What is the climate like?","What is the weather like?","What are the seasons like? How many and how long?","What are the birds like?","What are the small animals like?","What are the large animals like?"])
    if genre == "geography / natural resources":
        prompt=random.choice(["How are the continents laid out?","How are the countries laid out?","How much land is temperate, equatorial or polar?","Are there forests?","Are there tropical areas?","Are there grasslands or plains?","What natural resources are available in different regions?","Which natural resources are scarce?"])
    if genre == "magic / religion":
        prompt=random.choice(["Does magic exist? What constrains it?","What can magic not do?","Do people believe in one God, many or none?","Is there more than one religion?","Do people make sacrifices to Gods?","Do an elite control religion / magic or is it accessible to all?","Are there any magical creatures? Describe them.","To what extent is magic a learned skill or an innate talent?","Is magic a specialist, elite skill or is it used easily by commoners?","What is the price / cost of using magic?","Do magicians need to meet any specific criteria? Be celibate? Go through a ritual?","Does magic requires tools and props?","How is one magician stronger than another?","Can magic be combined to increase its strength?","What defeats magic?","Is magic admired / respected / feared / something else?","Is any magic illegal?","What is magic generally used for?","What are temples like?"])
    if genre == "population":
        prompt=random.choice(["Are there non-human sentient species? Describe them.","Did the people evolve on this planet or come from elsewhere?","What is the relationship between the different species?","Where and when did civilization begin?","What is the total population (of the planet / the country / the city, etc.)","What is the level of technology (stone age, hi tech)?"])
    if genre == "language / gestures":
        prompt=random.choice(["What languages to people speak?","Do most people speak more than one language?","Is there a common language? For trade?","How do people greet each other?","What is considered a rude gesture?","How do they curse? Gods? Body parts?","What titles / formalities are used?","What is a gesture of respect (bowing, saluting)?"])
    if genre == "culture":
        prompt=random.choice(["Do people live in happiness or fear?","Does the culture value strength or compassion more highly?","Does the culture value wealth or generosity more highly?","What are the common superstitions?","Are the people diverse or uniform?","How big is the gap between rich and poor?","What do people wear?","What is in fashion this year?","What was in fashion last year?","What topics of conversation are controversial?","Which topics of conversation are safe?","What constitutes a social faux pas?","What forms of art are there?","Is there theatre? Is it common or reserved for the wealthy?","What is a highly desirable job?","What is a lowly job?","What are the cities like, if any?","What are the houses like?","Do most people live in rural or urban areas?","Are there any domesticated animals?","Are there professional guilds / institutes/ etc?","How do you get into a professional guild?","What benefits do you gain from being a member of a guild?","Are criminals common or rare?","What calendar is used?"])
    if genre == "celebrations":
        prompt=random.choice(["What are the major festivals?","Describe a wedding.","Describe a funeral.","What are special celebratory foods?","What sort of clothes do people wear on special occasions?"])
    if genre == "education":
        prompt=random.choice(["Is there any formal education?","At what age do children start school?","Is education available to all or only certain groups?","Are different groups of people educated separately?","Is there a written language?","Are most people literate or illiterate?","What are schools like?","What are there different types of school for?"])
    if genre == "family":
        prompt=random.choice(["What is a normal family unit?","Do people marry for love or other reasons? What reasons?","Are the genders treated differently?","Who raises the children?"])
    if genre == "trade":
        prompt=random.choice(["What is the monetary system?","Are there multiple currencies?","Is there widespread trade?"])
    if genre == "conflict":
        prompt=random.choice(["Is there widespread conflict?","How long ago was the most recent war?","How damaging was the most recent war?","What was the cause of the most recent war?"])
    if genre == "governance":
        prompt=random.choice(["What is the system of government? Democracy? Dictatorship? Administration?","Is it a matriarchy or a patriarchy?","Does the leader have special protection (Kingsguard, secret service)?","How long has the system of government been in place?","Is there a class system? Different levels of citizenship?","Is there slavery?","Is there a form of police?","Is there a formal army?","How are wrongdoers tried and punished?","Does the government provide social assistance?","Is there any centralised healthcare?","Is there public transport?","Are there publicly run communications systems?","Do people trust the government?","Do the majority of people approve of or disapprove of the government?","Is social mobility easy or hard?","What is the system or taxation?","Does the government spy on its enemies? Its people?"])
    if genre == "foods and drink":
        prompt=random.choice(["What does a feast look like?","What does a basic pauper’s meal look like?","Do people mostly eat meat, fish or vegetables?","Do people eat plain or heavily flavoured food?","Do people eat together or separately?","Do people eat in small or large groups?","What utensils do people use to eat?","Are there many restaurants? Who goes to them?","Are there street food sellers?","What do people drink?","Is the water generally clean enough to drink?","Are some foods poisonous to certain people?","What are the tables like? Shape? High or low?","What is the general consensus on Brussel Sprouts?"])
    resp = 'I have a question about the {genrea} in your world. {prompta}'.format(genrea= genre, prompta= prompt)
    await ctx.send(resp)

def setup(bot):
    bot.add_command(prompt)
    bot.add_cog(Prompts(bot))