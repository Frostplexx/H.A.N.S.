import discord
from discord.ext import commands
from discord import channel


class TodoEditCog(commands.Cog, name="edit todo"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot
        
    @commands.command(name = "todoedit",
                    usage="(item)",
                    description = "edit your todo list")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def todoedit(self, ctx, item:str=None, new_message:str=None):
        channel =  ctx.channel
        #await ctx.message.delete
        async for messagelist in channel.history(limit=200):
            if (item + ".") in messagelist.content:
                await messagelist.edit(content=f"{item}. [ ] {(new_message)}")
        await ctx.channel.purge(limit = 1)



def setup(bot:commands.Bot):
	bot.add_cog(TodoEditCog(bot))