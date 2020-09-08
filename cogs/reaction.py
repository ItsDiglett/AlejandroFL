import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import os
import json
from config import dev
import time
import sqlite3
from datetime import datetime

class Example(commands.Cog):
        def __init__(self,client):
                self.client=client


        @commands.Cog.listener()
        async def on_raw_reaction_add(self, payload):
            message_id = payload.message_id
            if message_id == 691483280028991509:
                pair = {'🇦': 'League Of Legends','🇧': 'Minecraft','🇨': 'Destiny 2','🇩': 'Halo','🇪': 'Animal Crossing','🇫': 'PC','🇬': 'Xbox','🇭': 'PS4','🇮': 'Switch'}
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

                gaming = discord.utils.get(guild.roles, name=f'{pair[payload.emoji.name]}')   
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await member.add_roles(gaming)
  

            elif message_id == 691483294709055538:
                pair = {'🇦': 'FL-239','🇧': 'FL-305','🇨': 'FL-321','🇩': 'FL-352','🇪': 'FL-386','🇫': 'FL-407','🇬': 'FL-561','🇭': 'FL-689',
                    '🇮': 'FL-727','🇯': 'FL-754','🇰': 'FL-772','🇱': 'FL-786','🇲': 'FL-813','🇳': 'FL-850','🇴': 'FL-863','🇵': 'FL-904','🇶': 'FL-941','🇷': 'FL-954'}
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

                roless = discord.utils.get(guild.roles, name=f'{pair[payload.emoji.name]}')   
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await member.add_roles(roless)


            elif message_id == 691483319811964951:
                pair = {'💚': 'Green','❤️': 'Red','💙': 'Blue','⚪': 'White','🖤': 'Black','💜': 'Purple','🔶': 'Orange','💛': 'Yellow'}
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                colour = discord.utils.get(guild.roles, name=f'{pair[payload.emoji.name]}')   
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await member.add_roles(colour)

            elif message_id == 739704955706933280:
                pair = {'❌': 'NSFW','🌈': '🌈'}
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                NSFW = discord.utils.get(guild.roles, name=f'{pair[payload.emoji.name]}')   
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await member.add_roles(NSFW)

            elif message_id == 643944538833944606:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                if payload.emoji.name == '✅':
                    Role = guild.get_role(507597977754402846)
                    unverified = discord.utils.get(guild.roles, name='unverified')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Role)
                    await member.remove_roles(unverified)
                    embed = discord.Embed(
                    colour = 0xff0000
                    )                
                    embed.set_author(name=f'{member} has been verified.')
                    embed.set_thumbnail(url=(member.avatar_url))
                    embed.timestamp = datetime.utcnow()

                    channel = self.client.get_channel(658725663691505678)
                    await channel.send(embed=embed)


            

def setup(client):
    client.add_cog(Example(client))