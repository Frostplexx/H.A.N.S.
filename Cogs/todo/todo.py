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
        channel =  ctx.channel
        lastnumber = 0
        #go through the last 200 messages
        async for message in channel.history(limit=200):
            msg = message.content
            #splits message containing ! into a list and removes the !todo on the first item
            if "!" in msg:
                itemlist = msg.split(",")
                itemlist[0] = itemlist[0].replace("!todo ", "") 
                await message.delete()
            #find the biggest number, so that you can add items to current todo list
            elif int(msg[0]) > lastnumber: 
                lastnumber = int(msg[0])
        #combine all the strings :)
        for item in itemlist:
                await ctx.send(str(itemlist.index(item) + lastnumber + 1) + ". [ ] " + item)  
            


def setup(bot:commands.Bot):
	bot.add_cog(ChecklistCog(bot))