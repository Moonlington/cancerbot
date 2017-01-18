import asyncio, time, discord
import requests
import json
from geopy.geocoders import Nominatim
from discord.ext import commands
from .utils import checks

class Fun:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='ping', pass_context=True)
	async def ping(self, ctx):
		before = time.time() * 1000
		pingmsg = await self.bot.say('i am gay')
		after = time.time() * 1000
		await self.bot.edit_message(pingmsg, '_lol_ **{}ms**'.format(round(after - before)))

	@commands.command(name='weather', pass_context=True)
	async def weather(self, ctx, location:str):
		geolocator = Nominatim()
		location = geolocator.geocode(location)
		geo = geolocator.geocode(location)
		coordinates = '{},{}'.format(location.latitude, location.longitude)
		r = requests.get('https://api.darksky.net/forecast/removed/{}'.format(coordinates))
		jsondata = json.loads(r.text)
		data = '''
		:eggplant: :sweat_drops: {} (this is the fucking location you submitted edgy cunt)
		:eggplant: :sweat_drops: {} (wait, you don't know your timezone, then fucking read this you ignorant pussy)
		:eggplant: :sweat_drops: {} (kill yourself cunt, if you don't even know what this is already kill yourself none cares)
		:eggplant: :sweat_drops: {}° (none cares about this anyways smh)
		:eggplant: :sweat_drops: {}° (none cares about this anyways smh)
		'''.format(location.address, jsondata['timezone'], jsondata['currently']['summary'], round(jsondata['currently']['temperature']), round((int(jsondata['currently']['temperature'])-32)*5.0/9))
		msg = await self.bot.say('i am gay')
		await self.bot.edit_message(msg, '*_lol done you fuckin cunt, fucking kill yourself you fucking edgy fucking fucking fuckwad you fucking niggerfaggot_*\n{}'.format(data))

def setup(bot):
	bot.add_cog(Fun(bot))
