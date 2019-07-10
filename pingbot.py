import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "=")
User = "223398953549299712"
@client.command()
async def ping(ctx, amount):
    for x in range(int(amount)):
        await ctx.send("<@" + User + ">")

client.run("NTk4MTY5MjQ5ODc3NTkwMDI2.XSSumg.F__JzI-3t8LojWhd5w_K8uH7idM")