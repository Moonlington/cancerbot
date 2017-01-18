from discord.ext import commands
import discord
from cogs.utils import checks
import datetime, re
import json, asyncio
import copy
import logging
import traceback
import sys

initial_extensions = [
    'cogs.admin',
    'cogs.debug',
    'cogs.fun',
]

discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.CRITICAL)
log = logging.getLogger()
log.setLevel(logging.INFO)
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
log.addHandler(handler)

bot = commands.Bot(command_prefix=['cancerbot ', '!!'])

@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)
    
def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

credentials = load_credentials()

if __name__ == '__main__':
  for extension in initial_extensions:
    try:
      bot.load_extension(extension)
    except Exception as e:
      print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
  bot.run(credentials['token'])
