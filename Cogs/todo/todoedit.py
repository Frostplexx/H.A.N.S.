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
        #searches last 200 messages
        async for message in channel.history(limit=200):
                    msg = message.content
                    #if messages contains the command replace the command with empty = actual text to edit
                    if "!todoedit" in msg:
                        editmsg = msg.replace("!todoedit " + str(item), "")      
                    if (str(item) + "." + " [ ]") or str(item) + "." + " [✓]" in msg:
                        #if the messages contains the number to edit and actually is part of a todo list, edit that message to the new editmsg
                        await message.edit(content=f"{item}. [ ]{(editmsg)}")

        await ctx.channel.purge(limit = 1)
def setup(bot:commands.Bot):
	bot.add_cog(TodoEditCog(bot))