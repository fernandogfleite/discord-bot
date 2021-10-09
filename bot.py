import discord
import os
from decouple import config
from discord.ext import commands


TOKEN = config('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

def load_cogs(bot):
    bot.load_extension("manager")

    for file in os.listdir("commands"):
        if file.endswith('.py'):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")


load_cogs(bot)

bot.run(TOKEN)
