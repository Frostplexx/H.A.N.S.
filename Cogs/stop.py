import discord
from discord.ext import commands



class StopCog(commands.Cog, name="stop command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "stop",
                    usage="",
                    description = "stop music")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx):
        if ctx.voice_client.is_playing(): 
            ctx.voice_client.stop()


def setup(bot:commands.Bot):
	bot.add_cog(StopCog(bot))