import discord
from discord.ext import commands
from discord import channel

class DeleteCog(commands.Cog, name="delete"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot
    
    @commands.command(name = "delete",
                    usage="(item)",
                    description = "delete items")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def delete(self, ctx, item:int):
        channel =  ctx.channel
        #await ctx.message.delete
        async for message in channel.history(limit=200):
            #add a checkmark between the two brackets
            msg = message.content
            if (str(item) + "." + " [ ]") in msg or str(item) + "." + " [✓]" in msg:
                    for i in range(200): 
                        if (str(item + i) + ". [ ]") in msg:
                            editmsg = msg.replace(str(item + i) + "." + "[ ]", "")
                            message.edit(content=f"{item + i - 1}. [ ]{(editmsg)}")
                    await message.delete()
            if "!delete" in msg:
                await message.delete()


def setup(bot:commands.Bot):
	bot.add_cog(DeleteCog(bot))