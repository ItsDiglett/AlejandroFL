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

client.run(alejandro)