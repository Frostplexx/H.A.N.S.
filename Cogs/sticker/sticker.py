import discord
from discord.ext import commands
import json 
from random import randint



class StickerCog(commands.Cog, name="sticker command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "sticker",
                    usage="<name>",
                    description = "Send a sticker")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def sticker(self, ctx,sticker:str=None):
        if sticker is not None:
            with open("Cogs/sticker/stickers.json", "r") as config: 
                data = json.load(config)
                for item in data:
                    if sticker in item: 
                        await ctx.send(data[item])
                channel =  ctx.channel
            #searches last 200 messages
            async for message in channel.history(limit=200):
                if ("!sticker " + sticker) in message.content: 
                    await message.delete()
                    break
        else:
            stickerlist = ""
            with open("Cogs/sticker/stickers.json", "r") as file: 
                data = json.load(file)
                for item in data: 
                    stickerlist += item + ", "
            embed = discord.Embed(title=f"__**List of Stickers**__", description=f"{(stickerlist)}", color=randint(0, 0xffffff))
            await ctx.channel.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(StickerCog(bot))