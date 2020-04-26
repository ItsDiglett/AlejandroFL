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

print(os.getcwd())
client = commands.Bot(command_prefix = '/') 

for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

#@client.command() 
#async def Yes(ctx, amount= 5):
    #channel = client.get_channel(645172134125240341)
    #await channel.send('''
#__**Baby Alejandro Change Logs 3/3**__

#__**Github**__
#If for some reason you wanted to see the spaghetti I write, it's here:

#https://github.com/ItsDiglett/AlejandroFL
# ''')

client.run(alejandro)