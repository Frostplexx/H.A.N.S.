import discord
import json
from discord.ext import commands

with open("config.json", "r") as config: 
    data = json.load(config)
    commandslist = data["commands"]

class CommandListCog(commands.Cog, name="commands"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "commands",
                    usage="",
                    description = "list of aviable commands")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx):
        #read the cogs from the json and list them
        #this needs fixing
        final = ""
        for command in commandslist: 
            final += ("!" + command + ", ")
            final = final.replace("Cogs.", "")
        await ctx.send(final)


def setup(bot:commands.Bot):
	bot.add_cog(CommandListCog(bot))