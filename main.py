import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("==== Bot is ready ====")
    print("v0.1")

with open("token.txt") as file:
    token = file.read()

bot.run(token)