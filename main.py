import discord
from discord.ext import commands
import json
import asyncio
import threading
import time
import datetime


# Load config json and extract information
with open("config.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]
	initial_extensions = data["commands"]
with open("token.json", "r") as config:
		data = json.load(config)
		token = data["token"]

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()

bot = commands.Bot(prefix, intents = intents)

# Load cogs
loop = asyncio.get_event_loop()
print(initial_extensions)

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print(f"Failed to load extension {extension}")

#load reminders file
def load(): 
    with open("Cogs/reminders/reminders.json", "r") as data_file: 
                data = json.load(data_file)
    return data

#method to send a message to a given channel
async def signal(msg, channel_id):
	global bot # getting our bot variable from the global context
	channel = bot.get_channel(channel_id)
	await channel.send(msg)

#timer method that runn a loop in background every 0.6 seconds
def timer():
	print("ready!")
	while True:
		#tries to load json file and if it fails it passes on
		#otherwise it gives problems if you change something int the file
		try: 
			data = load()
		except: 
				pass
		#looks through all the variables/entries/reminders
		for item in data:
			today = str(datetime.datetime.today()).split(".")[0]
			#channel id from reminder entry
			chid = str(item).split(" ")[2]
			#date for when you should be reminded 
			date = str(item).split(" ")[0] + " " + str(item).split(" ")[1]
			#if the date is today/in this second
			if today in date:
				#make a new async task and call the signal method
				loop.create_task(signal(data[item], int(chid)))
				#delete the reminder
				del data[item]
				with open("Cogs/reminders/reminders.json", 'w') as data_file:
					data = json.dump(data, data_file, sort_keys=True, indent=4)
				break
		time.sleep(0.6)


@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))
	print(discord.__version__)
	#start the timer method as a backround task
	b = threading.Thread(name='background', target=timer)
	b.start()


bot.run(token)



