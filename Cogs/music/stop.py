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
        #stop the voice client,  when he is playing
        if ctx.voice_client.is_playing(): 
            ctx.voice_client.stop()
            await ctx.send("Music stopped!")


def setup(bot:commands.Bot):
	bot.add_cog(StopCog(bot))