import discord
from discord.ext import commands
import os
import random
import sqlite3
import Constants
import enum
from datetime import datetime

print(os.getcwd())
client = commands.Bot(command_prefix='/')
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def send(ctx):
    if ctx.message.author.id == 618897651026493441:
        await ctx.send('''__**Baby Alejandro Change Logs 9/7/20**__
    *I haven't done this in a while so it reflects a lot of changes in no particular order*
    • Fixed Reaction Role so it nested in a dictionary.
    •Created /v and /mv which creates votes and mod votes
    •Created /t which allows text-to-speech in vc.
    •Mod actions now log into a database and are viewable by /info.
    •Created /calc which does addition, subtraction, division, and multiplication.
    •Created /eightball which gives you your fortune.
    •Created /invite which makes one time invites to the server.
    • Fixed /help so now its a embed instead of a text block.

    Github
    If for some reason you wanted to see the spaghetti I write, it's here:

https://github.com/ItsDiglett/AlejandroFL
    ''')
client.run(Constants.AlEJANDROKEY)


























