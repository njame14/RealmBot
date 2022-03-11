# bot.py
import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from WoW import *

#Pull discord token and approved server from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='rb! ')
discord_servers = {}

#On bot startup
@bot.event
async def on_ready():
    global discord_servers
    #Count how many servers bot is connected to. 
    #Set realm_id to -1 to indicate not current realm is not set
    i = 0
    for guild in bot.guilds:
        i = i+1
        discord_servers.update({f'{guild.name}':-1})

    #Print all servers the bot is connected to
    print(f'{bot.user.name} has connected to Discord!\n'
        f'{bot.user.name} has connected to {i} servers!\n'
        f'\n{bot.user.name} is connected to the following guilds:')
    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')
    
    print(f'\n{bot.user.name} is now ready to rock!')


    
@bot.command(name = 'set')
async def set(ctx):
    global discord_servers
    await ctx.send(f'Please input your realm')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    msg = await bot.wait_for("message", check=check)
  
    realm = msg.content
    
    #Pulls the realm id
    #-1 if realm not found, 
    #Updates global discord_servers dictionary with realm id if found
    realm_id = getRealmID(realm)
    if realm_id == -1:
       response = "Realm could not be found, try again."
    else:
      discord_servers[f'{ctx.author.guild.name}'] = realm_id
      response = "Realm is set!"
    print(f'{ctx.author.guild.name},{realm_id}')
    await ctx.send(f'{ctx.author.mention}, {response}')

@bot.command(name = 'track')
async def track(ctx):
    realm_id = discord_servers[f'{ctx.author.guild.name}']
    if realm_id == -1:
        response = "Realm is not set!"
        await ctx.send(f'{ctx.author.mention}, {response}')
    else:
        await ctx.send(f'Tracking!')
        response = TrackRealm(realm_id)
        await ctx.send(f'@everyone,{response}')

    
@bot.command(name = 'status')
async def status(ctx):
    global discord_servers
    realm_id = discord_servers[f'{ctx.author.guild.name}']
    response = RealmStatus(realm_id)
    if (ctx.author.id == 145989557484126209):
        await ctx.send(f'Papa {ctx.author.mention}, {response}')
    else:
        await ctx.send(f'{ctx.author.mention}, {response}')


bot.run(TOKEN)






