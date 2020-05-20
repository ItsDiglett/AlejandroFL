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

        #One of these days I'll stop being a failure at life and actually code this correctly. 

        @commands.Cog.listener()
        async def on_raw_reaction_add(self, payload):
            message_id = payload.message_id
            if message_id == 708824729028526203:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                role = discord.utils.get(guild.roles, name=f'{payload.emoji.name}')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await member.add_roles(role)


            if message_id == 691483280028991509:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

                if payload.emoji.name == '🇦':
                    League = discord.utils.get(guild.roles, name='League Of Legends')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(League)
                elif payload.emoji.name =='🇧':
                    Minecraft = discord.utils.get(guild.roles, name='Minecraft')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Minecraft)
                elif payload.emoji.name =='🇨':
                    Destiny = discord.utils.get(guild.roles, name='Destiny 2')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Destiny)
                elif payload.emoji.name =='🇩':
                    Halo = discord.utils.get(guild.roles, name='Halo')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Halo)
                elif payload.emoji.name =='🇪':
                    AC = discord.utils.get(guild.roles, name='Animal Crossing')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(AC)            
                elif payload.emoji.name =='🇫':
                    PC = discord.utils.get(guild.roles, name='PC')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(PC)            
                elif payload.emoji.name =='🇬':
                    Xbox = discord.utils.get(guild.roles, name='Xbox')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Xbox)    
                elif payload.emoji.name =='🇭':
                    PS4 = discord.utils.get(guild.roles, name='PS4')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(PS4)     
                elif payload.emoji.name =='🇮':
                    Switch = discord.utils.get(guild.roles, name='Switch')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Switch)                
                else:
                    print('Not Ye')

            elif message_id == 691483294709055538:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                if payload.emoji.name == '🇦':
                    FL1 = discord.utils.get(guild.roles, name='FL-239')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL1)
                elif payload.emoji.name == '🇧':
                    FL2 = discord.utils.get(guild.roles, name='FL-305')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL2)
                elif payload.emoji.name == '🇨':
                    FL3 = discord.utils.get(guild.roles, name='FL-321')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL3)
                elif payload.emoji.name == '🇩':
                    FL4 = discord.utils.get(guild.roles, name='FL-352')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL4)
                elif payload.emoji.name == '🇪':
                    FL5 = discord.utils.get(guild.roles, name='FL-386')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL5)
                elif payload.emoji.name == '🇫':
                    FL6 = discord.utils.get(guild.roles, name='FL-407')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL6)
                elif payload.emoji.name == '🇬':
                    FL7 = discord.utils.get(guild.roles, name='FL-561')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL7)
                elif payload.emoji.name == '🇭':
                    FL8 = discord.utils.get(guild.roles, name='FL-689')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL8)
                elif payload.emoji.name == '🇮':
                    FL9 = discord.utils.get(guild.roles, name='FL-727')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL9)
                elif payload.emoji.name == '🇯':
                    FL10 = discord.utils.get(guild.roles, name='FL-754')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL10)
                elif payload.emoji.name == '🇰':
                    FL11 = discord.utils.get(guild.roles, name='FL-772')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL11)
                elif payload.emoji.name == '🇱':
                    FL12 = discord.utils.get(guild.roles, name='FL-786')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL12)
                elif payload.emoji.name == '🇲':
                    FL13 = discord.utils.get(guild.roles, name='FL-813')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL13)
                elif payload.emoji.name == '🇳':
                    FL14 = discord.utils.get(guild.roles, name='FL-850')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL14)
                elif payload.emoji.name == '🇴':
                    FL15 = discord.utils.get(guild.roles, name='FL-863')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL15)
                elif payload.emoji.name == '🇵':
                    FL16 = discord.utils.get(guild.roles, name='FL-904')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL16)
                elif payload.emoji.name == '🇶':
                    FL17 = discord.utils.get(guild.roles, name='FL-941')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL17)
                elif payload.emoji.name == '🇷':
                    FL18 = discord.utils.get(guild.roles, name='FL-954')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL18)

            elif message_id == 691483319811964951:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                if payload.emoji.name=='💚':
                    Green = discord.utils.get(guild.roles, name='Green')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Green)   
                elif payload.emoji.name == '❤':  
                    Red = discord.utils.get(guild.roles, name='Red')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Red)
                elif payload.emoji.name == '💙':
                    Blue = discord.utils.get(guild.roles, name='Blue')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Blue)
                elif payload.emoji.name == '⚪':
                    White = discord.utils.get(guild.roles, name='White')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(White)
                elif payload.emoji.name == '🖤':
                    Black = discord.utils.get(guild.roles, name='Black')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Black)
                elif payload.emoji.name == '💜':
                    Purple = discord.utils.get(guild.roles, name='Purple')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Purple)
                elif payload.emoji.name == '🔶':
                    FL18 = discord.utils.get(guild.roles, name='Orange')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(FL18)
                elif payload.emoji.name == '💛':
                    Yellow = discord.utils.get(guild.roles, name='Yellow')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.add_roles(Yellow)

            elif message_id == 691483331073933372:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

                if payload.emoji.name == '❌':
                    NSFW = discord.utils.get(guild.roles, name='NSFW')   
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