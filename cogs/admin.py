from discord.ext import commands
from .utils import checks
import discord
import subprocess
import sys
import os

class Admin:
    """Admin-only commands that make the bot dynamic."""

    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(hidden=True)
    async def load(self, *, module : str):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await self.bot.say('\N{PISTOL}')
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('\N{OK HAND SIGN}')

    @checks.is_owner()
    @commands.command(hidden=True)
    async def unload(self, *, module : str):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await self.bot.say('\N{PISTOL}')
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('\N{OK HAND SIGN}')

    @checks.is_owner()
    @commands.command(name='reload', hidden=True)
    async def _reload(self, *, module : str):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await self.bot.say('\N{PISTOL}')
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('\N{OK HAND SIGN}')

    @checks.is_owner()
    @commands.command(name='update', hidden=True)
    async def update(self):
        subprocess.Popen('sudo git pull', shell=True, executable='/bin/bash)
        await self.bot.say(update, 'updating')
        os.execl(sys.executable, sys.executable, * sys.argv)
        
def setup(bot):
    bot.add_cog(Admin(bot))
