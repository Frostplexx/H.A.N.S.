import discord
from discord.ext import commands


class templateCog(commands.Cog, name="template command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "template",
                    usage="",
                    description = "Say template to the bot")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def template(self, ctx):
        await ctx.send()


def setup(bot:commands.Bot):
	bot.add_cog(templateCog(bot))