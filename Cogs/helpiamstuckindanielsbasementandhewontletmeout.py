import discord
from discord.ext import commands
from discord import channel

class HelloCog(commands.Cog, name="helpiamstuckindanielsbasementandhewontletmeout"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "helpiamstuckindanielsbasementandhewontletmeout",
                    usage="",
                    description = "helpiamstuckindanielsbasementandhewontletmeout")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx):
        await ctx.send("stfu philip")
        await ctx.send("you are mine now")
        await ctx.send(file=discord.File('tenor.gif'))


def setup(bot:commands.Bot):
	bot.add_cog(HelloCog(bot))