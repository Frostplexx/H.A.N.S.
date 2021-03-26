import discord
from discord.ext import commands
from discord import channel


class UnTickCog(commands.Cog, name="untick"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot
    
    @commands.command(name = "untick",
                    usage="(item)",
                    description = "untick items")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def todoedit(self, ctx, item:str=None):
        channel =  ctx.channel
        #same as tick but replaces the checkmark with emptyness
        async for message in channel.history(limit=200):
            if (item + ".") in message.content and "✓" in message.content:                     
                    new_message = message.content.replace("✓", " ")
                    await message.edit(content=f"{(new_message)}")
            #delete the untick command
            if "!untick" in message.content:
                await message.delete()          



def setup(bot:commands.Bot):
	bot.add_cog(UnTickCog(bot))