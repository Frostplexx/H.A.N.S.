import discord
from discord.ext import commands
from discord import channel


class TickCog(commands.Cog, name="tick "): 
    def __init__(self, bot:commands.bot):
        self.bot = bot
    
    @commands.command(name = "tick",
                    usage="(item)",
                    description = "tick todo items")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def todoedit(self, ctx, item:str=None):
        channel =  ctx.channel
        #await ctx.message.delete
        async for message in channel.history(limit=200):
            if (item + ".") in message.content and "✓" not in message.content:
                index = message.content.find("]")
                new_message = message.content[:index] + "✓" +  message.content[index:]
                new_message = new_message.replace("[ ", "[")
                await message.edit(content=f"{(new_message)}")

            if "!" in message.content:
                await message.delete()    

def setup(bot:commands.Bot):
	bot.add_cog(TickCog(bot))