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

class Example(commands.Cog):
        def __init__(self,client):
                self.client=client

        @commands.Cog.listener()
        async def on_raw_reaction_remove(self, payload):
            message_id = payload.message_id
            if message_id == 646833893382553600:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

                if payload.emoji.name == '🇦':
                    League = discord.utils.get(guild.roles, name='League Of Legends')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(League)
                elif payload.emoji.name =='🇧':
                    Minecraft = discord.utils.get(guild.roles, name='Minecraft')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Minecraft)
                elif payload.emoji.name =='🇨':
                    Destiny = discord.utils.get(guild.roles, name='Destiny 2')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Destiny)
                elif payload.emoji.name =='🇩':
                    Halo = discord.utils.get(guild.roles, name='Halo')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Halo)
                elif payload.emoji.name =='🇪':
                    PC = discord.utils.get(guild.roles, name='PC')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(PC)            
                elif payload.emoji.name =='🇫':
                    Xbox = discord.utils.get(guild.roles, name='Xbox')
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Xbox)            
                elif payload.emoji.name =='🇬':
                    PS4 = discord.utils.get(guild.roles, name='PS4')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(PS4)    
                elif payload.emoji.name =='🇭':
                    Switch = discord.utils.get(guild.roles, name='Switch')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Switch)                        
                else:
                    print('Not Ye')

            elif message_id == 646833893890326538:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                if payload.emoji.name == '🇦':
                    FL1 = discord.utils.get(guild.roles, name='FL-239')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL1)
                elif payload.emoji.name == '🇧':
                    FL2 = discord.utils.get(guild.roles, name='FL-305')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL2)
                elif payload.emoji.name == '🇨':
                    FL3 = discord.utils.get(guild.roles, name='FL-321')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL3)
                elif payload.emoji.name == '🇩':
                    FL4 = discord.utils.get(guild.roles, name='FL-352')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL4)
                elif payload.emoji.name == '🇪':
                    FL5 = discord.utils.get(guild.roles, name='FL-386')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL5)
                elif payload.emoji.name == '🇫':
                    FL6 = discord.utils.get(guild.roles, name='FL-407')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL6)
                elif payload.emoji.name == '🇬':
                    FL7 = discord.utils.get(guild.roles, name='FL-561')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL7)
                elif payload.emoji.name == '🇭':
                    FL8 = discord.utils.get(guild.roles, name='FL-689')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL8)
                elif payload.emoji.name == '🇮':
                    FL9 = discord.utils.get(guild.roles, name='FL-727')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL9)
                elif payload.emoji.name == '🇯':
                    FL10 = discord.utils.get(guild.roles, name='FL-754')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL10)
                elif payload.emoji.name == '🇰':
                    FL11 = discord.utils.get(guild.roles, name='FL-772')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL11)
                elif payload.emoji.name == '🇱':
                    FL12 = discord.utils.get(guild.roles, name='FL-786')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL12)
                elif payload.emoji.name == '🇲':
                    FL13 = discord.utils.get(guild.roles, name='FL-813')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL13)
                elif payload.emoji.name == '🇳':
                    FL14 = discord.utils.get(guild.roles, name='FL-850')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL14)
                elif payload.emoji.name == '🇴':
                    FL15 = discord.utils.get(guild.roles, name='FL-863')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL15)
                elif payload.emoji.name == '🇵':
                    FL16 = discord.utils.get(guild.roles, name='FL-904')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL16)
                elif payload.emoji.name == '🇶':
                    FL17 = discord.utils.get(guild.roles, name='FL-941')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL17)
                elif payload.emoji.name == '🇷':
                    FL18 = discord.utils.get(guild.roles, name='FL-954')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL18)

            elif message_id == 646833894255230976:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                if payload.emoji.name=='💚':
                    Green = discord.utils.get(guild.roles, name='Green')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Green)   
                elif payload.emoji.name == '❤':  
                    Red = discord.utils.get(guild.roles, name='Red')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Red)
                elif payload.emoji.name == '💙':
                    Blue = discord.utils.get(guild.roles, name='Blue')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Blue)
                elif payload.emoji.name == '⚪':
                    White = discord.utils.get(guild.roles, name='White')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(White)
                elif payload.emoji.name == '⚫':
                    Black = discord.utils.get(guild.roles, name='Black')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Black)
                elif payload.emoji.name == '💜':
                    Purple = discord.utils.get(guild.roles, name='Purple')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Purple)
                elif payload.emoji.name == '🔶':
                    FL18 = discord.utils.get(guild.roles, name='Orange')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(FL18)
                elif payload.emoji.name == '💛':
                    Yellow = discord.utils.get(guild.roles, name='Yellow')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(Yellow)

            elif message_id == 646833894917931036:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
                emoji = self.client.get_emoji(id=643570826683351050)
                if payload.emoji == emoji:
                    NSFW = discord.utils.get(guild.roles, name='NSFW')   
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    await member.remove_roles(NSFW)



def setup(client):
    client.add_cog(Example(client))



