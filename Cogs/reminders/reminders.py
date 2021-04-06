import discord
from discord.ext import commands
import json
from random import randint

class RemindersCog(commands.Cog, name="Reminders command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "reminders",
                    usage="",
                    description = "Say Reminders to the bot")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def Reminders(self, ctx):

        with open("Cogs/reminders/reminders.json", "r") as data_file: 
            data = json.load(data_file)

        embed = discord.Embed(title=f"Active Reminders: ", color=randint(0, 0xffffff))    
    
        if len(data) > 0: 
            for items in data:
                    name = str(data).replace("{'", "").split(" ")[0] + " " + str(data).replace("{'", "").split(" ")[1]
                    embed.add_field(name=f"{(name)}", value=f"{(data[items])}", inline=False)                 
            await ctx.channel.send(embed=embed)
        else: 
            await ctx.send("No active Reminders!")

def setup(bot:commands.Bot):
	bot.add_cog(RemindersCog(bot))