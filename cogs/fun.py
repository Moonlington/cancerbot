import asyncio, time, discord
from discord.ext import commands
from .utils import checks

class Fun:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='ping', pass_context=True, hidden=True)
	async def ping(self, ctx):
		before = time.time() * 1000
		pingmsg = await self.bot.say('i am gay')
		after = time.time() * 1000
		await self.bot.edit_message(pingmsg, '_lol_ **{}ms**'.format(round(after - before)))

def setup(bot):
	bot.add_cog(Fun(bot))
