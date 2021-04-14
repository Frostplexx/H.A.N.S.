import discord
from discord.ext import commands
import json 
from random import randint
from discord.guild import Guild


class StickerCog(commands.Cog, name="sticker command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "sticker",
                    usage="<name>",
                    description = "Send a sticker")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def sticker(self, ctx,sticker:str=None):
        #load and send the image  
        channel =  ctx.channel
        guild = ctx.guild       
        if sticker is not None:
            async for message in channel.history(limit=200):
                #searches last 200 messages
                #delete the original command
                if ("!sticker " + sticker) in message.content:
                    await message.delete()
                    member = await guild.fetch_member(message.author.id)
                    nick = member.display_name
                    break

            with open("Cogs/sticker/stickers.json", "r") as config: 
                data = json.load(config)
                for item in data:
                    if sticker in item: 
                        await ctx.send(nick + ":")
                        await ctx.send(data[item])


        #if no sticker name is given send a list of aviable stickers
        else:
            stickerlist = ""
            with open("Cogs/sticker/stickers.json", "r") as file: 
                data = json.load(file)
                for item in data: 
                    stickerlist += item + ", "
            embed = discord.Embed(title=f"__**List of Stickers**__", description=f"{(stickerlist)}", color=randint(0, 0xffffff))
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/822577638098993192/826453061932810312/Instagram-UI_sticker-512.png")
            await ctx.channel.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(StickerCog(bot))