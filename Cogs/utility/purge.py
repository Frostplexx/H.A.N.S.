import discord
from discord.ext import commands

class PurgeCog(commands.Cog, name="purge command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "purge",
                    usage="<number of messages to purge>",
                    description = "Purge messages")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx, amount:str):
        #purge set amount of messages + itself
        if amount == "all":
            await ctx.channel.purge()
        elif amount.isnumeric(): 
            await ctx.channel.purge(limit = int(amount) + 1)
        else: 
            await ctx.send("Usage: !purge <amount> or !purge all")
        
def setup(bot:commands.Bot):
	bot.add_cog(PurgeCog(bot))