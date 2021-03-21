from discord.ext import commands
from music_handler import MHandler
import discord



class PlayCog(commands.Cog, name="play command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "play",
                    usage="<url>",
                    description = "play music!")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def play(self, ctx, *, url):
        channel = ctx.message.author.voice.channel

        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(channel)
        else: 
            await channel.connect()

        if ctx.voice_client.is_playing(): 
            MHandler.queue.append(url)
            print(MHandler.queue)
            await ctx.send("Song added to queue! Write !queue to view it")
        else:
            MHandler.queue.append(url)
            await MHandler.play(self, ctx)
    



def setup(bot:commands.Bot):
	bot.add_cog(PlayCog(bot))