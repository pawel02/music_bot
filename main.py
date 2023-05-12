import discord
from discord.ext import commands
import os
# added to allow the cogs to be force-added later
import asyncio

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='/')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
async def setup(bot):
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))

#start the bot with our token
asyncio.run(setup(bot))
bot.run(os.getenv("TOKEN"))
