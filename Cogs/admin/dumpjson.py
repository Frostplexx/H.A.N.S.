import discord
from discord.ext import commands
import json

class Dumpjson(commands.Cog, name="dumpjson command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "dumpjson",
                    usage="",
                    description = "Say dumpjson to the bot")
    @commands.has_role("Admin")
    @commands.cooldown(1, 2, commands.BucketType.member)
        #send content of all json files
        async def dumpjson(self, ctx):
            pass
def setup(bot:commands.Bot):
	bot.add_cog(Dumpjson(bot))