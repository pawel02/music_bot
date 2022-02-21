import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix="/")

@Bot.command()
async def echo(ctx, *args):
    _args = " ".join(args)
    await ctx.send(_args)

token = ""
with open("token.txt", "r") as file:
    token = file.readline()

Bot.run(token)
