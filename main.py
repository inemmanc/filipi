import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("==== Bot is ready ====")

bot.run("MTI5ODA5Mjg5MzIxMDQxNTExNA.GmwVr1.HEVSJI4YNdGRWC9cdYtPlclQym6LN2JBApjIk0")