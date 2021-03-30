import discord
from discord.ext import commands
import json 
from random import randint

with open("Cogs/misc/stickers.json", "r") as config: 
    data = json.load(config)
    stickers = data["stickers"]

class StickerCog(commands.Cog, name="sticker command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "sticker",
                    usage="",
                    description = "Send a sticker")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def sticker(self, ctx,sticker:str=None):
        if sticker is not None:
            for item in stickers:
                if sticker in item: 
                    await ctx.send(item[sticker])
            channel =  ctx.channel
            #searches last 200 messages
            async for message in channel.history(limit=200):
                if ("!sticker " + sticker) in message.content: 
                    await message.delete()
                    break
        else:
            embed = discord.Embed(title=f"__**List of Stickers**__", description=f"**fabian, math**", color=randint(0, 0xffffff))
            await ctx.channel.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(StickerCog(bot))