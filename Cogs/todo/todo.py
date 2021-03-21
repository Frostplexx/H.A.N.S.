import discord
from discord.ext import commands
from discord import channel

class ChecklistCog(commands.Cog, name="checklist command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "todo",
                    usage="<item1,item2,item3>",
                    description = "add items to checklist checklist")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def todo(self, ctx, items:str):
        #message.content.split makes more sense and actually probably works
        channel =  ctx.channel
        lastnumber = 0
        async for message in channel.history(limit=200):
            msg = message.content
            #splits message containing ! into a list and removes the !todo on the first item
            if "!" in msg:
                itemlist = msg.split(",")
                itemlist[0] = itemlist[0].replace("!todo ", "") 
                await message.delete()          
            elif int(msg[0]) > lastnumber: 
                lastnumber = int(msg[0])
        for item in itemlist:
                await ctx.send(str(itemlist.index(item) + lastnumber + 1) + ". [ ] " + item)  
            


def setup(bot:commands.Bot):
	bot.add_cog(ChecklistCog(bot))