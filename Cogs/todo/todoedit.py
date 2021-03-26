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
    async def todoedit(self, ctx, item:int=0):
        channel =  ctx.channel
        #doesnt work pls fix :(
        async for message in channel.history(limit=200):
                    msg = message.content
                    if "!todoedit" in msg:
                        editmsg = msg.replace("!todoedit " + str(item), "")      
                    if (item + ".") in msg:
                        await message.edit(content=f"{item}. [ ] {(editmsg)}")

        await ctx.channel.purge(limit = 1)
def setup(bot:commands.Bot):
	bot.add_cog(TodoEditCog(bot))