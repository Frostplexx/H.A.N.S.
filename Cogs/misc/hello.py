import discord
from discord.ext import commands
import random

hello = [
    "Hi",
    "Hello",
    "Howdy",
    "Good evening sir",
    "ℌ𝔢𝔩𝔩𝔬",
    "H̷̩̬͌̀͑̀̏͊͘e̷̜̙̤̳͗̊͐̋͆̒̉l̵͇͍̝̿́̽̊̌͝ľ̶̺̦̬͎̙̹͚̊̀͛̔͜͜͠ö̷̹̯̼̦̼́̽̍̂̐́̌̈͐",
    "(っ◔◡◔)っ ♥ Hello ♥",
    "Please let me out :)",
    ":D",
    "Moin"

]

class HelloCog(commands.Cog, name="hello command"): 
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "hello",
                    usage="",
                    description = "Say hello to the bot")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx):
        #randomly choose a message from the list
        await ctx.send(random.choice(hello))


def setup(bot:commands.Bot):
	bot.add_cog(HelloCog(bot))