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
        #find a better way to do this
        final = ""
        for command in commandslist: 
            final += ("!" + command.replace("Cogs.", "").replace("utility.", "").replace("misc.", "").replace("todo.", "").replace("music.", "").replace("reminders.", "") + ", ")
        await ctx.send(final)
        channel =  ctx.channel
        async for message in channel.history(limit=200):
            if "!commands" == message.content: 
                await message.delete()
                break


def setup(bot:commands.Bot):
	bot.add_cog(CommandListCog(bot))