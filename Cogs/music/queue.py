import discord
from discord.ext import commands
from music_handler import MHandler
from random import randint


class QueueCog(commands.Cog, name="queue command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "queue",
                    usage="",
                    description = "View music queue!")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx):
        embed = discord.Embed(title=f"__**Songs in Queue:**__", color=randint(0, 0xffffff))
        embed.set_thumbnail(url=f'https://freeiconshop.com/wp-content/uploads/edd/music-quavers-flat.png')
        if len(MHandler.queue) < 2: 
            await ctx.send("Queue is empty!")
        else: 
            for song in MHandler.queue:
                player = await MHandler.from_url(song, loop=self.bot.loop, stream=True)        
                embed.add_field(name=f"{(MHandler.queue.index(song) + 1 )}. {(player.title)} ", value=f"{(song)}", inline=False)
            await ctx.channel.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(QueueCog(bot))