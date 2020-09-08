import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import dev
import asyncio
import os
import random
import time
import sqlite3
import json
from datetime import datetime
import gtts
from actions import Modactions
from embedcreator import Log
import Constants



class GeneralUse(commands.Cog):
        def __init__(self,client):
                self.client=client

        @commands.command()
        async def calc(self, ctx, x:int, sign, y:int):
            if sign == '/':
                z = x / y
            elif sign == '*':
                z = x * y
            elif sign == '+':
                z = x + y
            elif sign == '-':
                z = x - y
            await ctx.send(z)

        @commands.command()
        async def eightball(self,ctx):
            if ctx.message.channel.id ==750028390039420979:
                reponses = {1:'It is certain.', 2:'It is decidedly so.', 3:'Without a doubt.',  4:"Don't count on it.", 5:'Ask Again Later.', 6:'My reply is no.', 7:'My sources say no.', 8:'This is the way.'}
                rand = random.randint(1, 8)
                await ctx.send(reponses[rand])
            else:
                pass

        @commands.command()
        async def invite(self, ctx):
                inivte = await ctx.channel.create_invite(reason=None, max_age=86400,max_uses=1)
                await ctx.message.author.send(f'This is a one time invite link that expires in 1 day.\n{inivte.url}')

        @commands.command(pass_context=True,name="help", help="returns all commands available")
        async def help(self, ctx):
            embed = discord.Embed(
            colour = Constants.ROLE_COLOUR
            )
            for command in self.client.commands:
                embed.add_field(name=f'/{command}', value=command.help, inline=False)

            await ctx.message.author.send(embed=embed)    

def setup(client):
        client.add_cog(GeneralUse(client))