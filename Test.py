
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Protecting The Server'))
    print('Bot is ready.')

client.run(TOKEN)
