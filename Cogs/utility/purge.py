import discord
from discord.ext import commands

class PurgeCog(commands.Cog, name="purge command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "purge",
                    usage="<number of messages to purge>",
                    description = "Purge messages")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx, amount:int):
        #purge set amount of messages + itself
        await ctx.channel.purge(limit = amount + 1)


def setup(bot:commands.Bot):
	bot.add_cog(PurgeCog(bot))