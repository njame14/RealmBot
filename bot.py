# bot.py
import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from WoW import SetRealm
from WoW import RealmStatus

#Pull discord token and approved server from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='rb! ')


@bot.event
async def on_ready():
    SetRealm("NA")
    RealmStatus()
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f'{bot.user.name} has connected to Discord!\n'
        f'{bot.user} is connected to the following guilds:\n'
        f'{guild.name}(id: {guild.id})\n'
        f'{bot.user.name} is now ready to rock!'
    )


    
@bot.command(name = 'set')
async def set(ctx):
    await ctx.send(f'Please input your realm')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    msg = await bot.wait_for("message", check=check)
    realm = msg.content
    response = SetRealm(realm)
    await ctx.send(f'{ctx.author.mention}, {response}')


        

@bot.command(name = 'status')
async def status(ctx):
    response = RealmStatus()
    if (ctx.author.id == 145989557484126209):
        await ctx.send(f'Papa {ctx.author.mention}, {response}')
    else:
        await ctx.send(f'{ctx.author.mention}, {response}')


bot.run(TOKEN)






