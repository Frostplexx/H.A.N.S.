import discord
from discord.ext import commands
import json


class StaddCog(commands.Cog, name="stadd command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "stadd",
                    usage="",
                    description = "Add sticker")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def stadd(self, ctx, name:str=None):
        #get the url from the attachemnt
        url = ctx.message.attachments[0].url
        final = {name : url}
        #add url and sticker name to json
        with open("Cogs/sticker/stickers.json", "r+") as file: 
            data = json.load(file)
            data.update(final)
            file.seek(0)
            json.dump(data, file, sort_keys=True, indent=4)
            await ctx.send("Sticker " + name + " added successfully!")

def setup(bot:commands.Bot):
	bot.add_cog(StaddCog(bot))