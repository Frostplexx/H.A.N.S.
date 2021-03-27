import discord
from discord.ext import commands
from music_handler import MHandler


class ClearCog(commands.Cog, name="clear command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "clear",
                    usage="",
                    description = " clear queue")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def clear(self, ctx):
        if len(MHandler.queue) > 2:
            #delete all items from queue except the one currently playing 
            MHandler.queue = [x for i,x in enumerate(MHandler.queue) if i!=MHandler.index]
            await ctx.send("Emptied Queue!")
        else:
            await ctx.send("Queue is empty!")





def setup(bot:commands.Bot):
	bot.add_cog(ClearCog(bot))
