import discord
from discord.ext import commands
from discord import channel


class TickallCog(commands.Cog, name="untickall "): 
    def __init__(self, bot:commands.bot):
        self.bot = bot
    
    @commands.command(name = "untickall",
                    usage="",
                    description = "untickall items")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def todoedit(self, ctx):
        channel =  ctx.channel
        #await ctx.message.delete
        async for message in channel.history(limit=200):
            #add a checkmark between the two brackets
            if (". [✓]") in message.content:
                new_message = message.content.replace("✓", " ")
                await message.edit(content=f"{(new_message)}")
            #delete the command message
            if "!untickall" in message.content:
                await message.delete()    

    
def setup(bot:commands.Bot):
	bot.add_cog(TickallCog(bot))