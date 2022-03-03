# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from WoW import ServerStatus

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='rb!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f'{bot.user.name} has connected to Discord!\n'
        f'{bot.user} is connected to the following guilds:\n'
        f'{guild.name}(id: {guild.id})\n'
        f'{bot.user.name} is now ready to rock!'
    )

@bot.command(name = 'sleep')
async def sleep(ctx):
    await ctx.send('👍')
    await ctx.send(f'https://tenor.com/view/stanley-sleeping-the-office-gif-10555880')
    await bot.close()

@bot.command(name = 'status')
async def status(ctx):
    response = ServerStatus()
    if(ctx.author.id == 145984332568199169):
        await ctx.send(f'Hey Uncle {ctx.author.mention}!, {response}')
    elif(ctx.author.id == 320025745143365633):
        await ctx.send(f' {ctx.author.mention} {response}')
    elif (ctx.author.id == 145989557484126209):
        await ctx.send(f'In nomine Patris et Filii et Spiritus Sancti. \n Honorable {ctx.author.mention}, {response}')
    else:
        await ctx.send(f'{ctx.author.mention}, {response}')

    role = discord.utils.get(ctx.guild.roles, name="Gal1")
    if(role in ctx.author.roles):
        await ctx.send(f'Girl Gamer')


bot.run(TOKEN)






