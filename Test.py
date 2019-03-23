
import discord
from discord.ext import commands

TOKEN = 'NTU5MDM5MDUwOTU5MjkwMzc4.D3fmGA.2zAs-gytNnH6QPJboHUI9yCW3S8'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Protecting The Server'))
    print('Bot is ready.')

client.run('NTU5MDM5MDUwOTU5MjkwMzc4.D3fmGA.2zAs-gytNnH6QPJboHUI9yCW3S8')
