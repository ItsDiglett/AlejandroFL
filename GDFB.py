import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
from config import alejandro, zone, Malay
import random
import time
import math
import sqlite3
import json

print(os.getcwd())
client = commands.Bot(command_prefix = '/') 

for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(643908047202287636) #leaves
    channel2 = client.get_channel(643915842865856524) #members channel
    embed = discord.Embed(
    colour = 0xff0000
    )                
    embed.set_author(name=f'{member} has left the server')
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text=(time.ctime()))   

    await channel.send(embed=embed)
    await channel2.edit(name= f'Members: {member.guild.member_count} ')

@client.event
async def on_message(message):
    if message.content.startswith('/v'):
        creator = discord.utils.get(message.guild.roles, name ="Creators")
        if creator in message.author.roles:
            await message.add_reaction('✅')
            await message.add_reaction('🇽')
        else:
            await asyncio.sleep(0.01)
            print('It worked')
    else:
        await asyncio.sleep(0.01)

    await client.process_commands(message)

#@client.command()
#async def Yes(ctx, amount= 5):
    #channel = client.get_channel(645172134125240341)
    #await channel.send('''
#__**Baby Alejandro Change Logs (Hotfix 11/19)v2**__   

#__**Github**__
#If for some reason you wanted to see the spaghetti I write, it's here:
#https://github.com/ItsDiglett/AlejandroFL
#  ''')

client.run(alejandro)