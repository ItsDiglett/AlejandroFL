import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
from config import alejandro
import random
import math
import sqlite3
import json
from datetime import datetime, timedelta
import time
import gtts

print(os.getcwd())
client = commands.Bot(command_prefix = '/') 


for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_member_remove(member):
    bot = await client.fetch_user(618903054506393640)
    channel = client.get_channel(643908047202287636) #leaves
    channel2 = client.get_channel(643915842865856524) #members channel
    embed = discord.Embed(
    colour = 0xff0000
    )                
    embed.set_author(name=f'{member} has left the server')
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text=f'{bot}', icon_url=(bot.avatar_url))
    embed.timestamp = datetime.utcnow()

    await channel.send(embed=embed)
    await channel2.edit(name= f'Members: {member.guild.member_count} ')

client.run(alejandro)