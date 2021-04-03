import discord
from discord.ext import commands
import time
import datetime

#reminder = [in/on, days, and, hours/dd.mm, string]
class ReminderCog(commands.Cog, name="reminder command"):

    def __init__(self, bot:commands.bot):
        self.bot = bot
    @commands.command(name = "remindme",
                    usage=" in/on day/hours/minutes/dd.mm,  <reminder>",
                    description = "Say reminder to the bot")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def reminder(self, ctx):
        rmdatetime = ""
        rmtext = ""
        today = datetime.datetime.today()

        channel =  ctx.channel
        #searches last 200 messages
        async for message in channel.history(limit=200):
            msg = message.content
            if "!remindme" in msg:
                reminder = msg.split(" ")
                del reminder[0]
                print(reminder)

            if reminder[0] == "in" and reminder[3] != "and":
                if reminder [2] == "hour" or reminder[2] == "hours": 
                    time_change = datetime.timedelta(hours=int(reminder[1]))
                elif reminder [2] == "minute" or reminder[2] == "minutes": 
                    time_change = datetime.timedelta(minutes=int(reminder[1]))
                rmdatetime = today + time_change
            elif reminder[0] == "in" and reminder[3] == "and":
                print("test")
            elif reminder[0] == "on": 
                day = str(reminder[1]).split(".")[0]
                month = str(reminder[1]).split(".")[1]
                if reminder[2] == "at": 
                    hour = str(reminder[3]).split(":")[0]
                    minute = str(reminder[3]).split(":")[1]                    
                else: 
                    hour = "12"
                    minute = "00"
                rmdatetime = datetime.datetime(2021,int(month), int(day),int(hour), int(minute))


            print("Reminder set for: " + str(rmdatetime))
            print("Today is: " + str(today) + " " + str(datetime.datetime.now()))

            break; 
                     




def setup(bot:commands.Bot):
	bot.add_cog(ReminderCog(bot))