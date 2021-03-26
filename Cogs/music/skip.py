import discord
from discord.ext import commands
from music_handler import MHandler


class SkipCog(commands.Cog, name="skip command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "skip",
                    usage="",
                    description = " skip music")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def skip(self, ctx):
        #increment the playing index and restart song
        if MHandler.index < len(MHandler.queue) - 1:
            if ctx.voice_client.is_playing(): 
                ctx.voice_client.stop()
                MHandler.index += 1
            await MHandler.play(self, ctx)
        else: 
            await ctx.send("This is the last song!")




def setup(bot:commands.Bot):
	bot.add_cog(SkipCog(bot))
