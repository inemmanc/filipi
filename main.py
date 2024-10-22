import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="filipi ", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("==== Bot is ready ====")
    print("v0.1")

@bot.command(aliases=["Ping", "Pping", "PING", ""])
async def ping(ctx):
    ping_embed = discord.Embed(title="Ping test", description="Latency", color=discord.Color.green())
    ping_embed.add_field(name="Bot latency (ms): ", value=f"{round(bot.latency * 1000)}ms.", inline=True)
    ping_embed.set_footer(text=f"Requested: {ctx.author.name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=ping_embed)

with open("token.txt") as file:
    token = file.read()

bot.run(token)