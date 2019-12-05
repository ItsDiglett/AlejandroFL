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
        async def on_ready(self):
                print('It\'s alive!')
                
        #This is logs the message deletes. Sends Logs to Florida Control Room
        @commands.Cog.listener()
        async def on_message_delete(self, message = discord.Message):
                channel = self.client.get_channel(643907846651772948) #message-deletes in Florida Control room
                if message.guild.id == 504052021683290125:                
                        if not message.attachments:
                                
                                embed = discord.Embed(
                                colour = 0xff0000
                                )
                                embed.set_author(name=(message.author), icon_url=(message.author.avatar_url))
                                embed.add_field(name=(f'Message was deleted'), value=(message.content), inline=False)
                                embed.set_footer(text=(time.ctime()))

                                await channel.send(embed=embed)
                        else:        
                                embed1 = discord.Embed(
                                colour = 0xff0000

                                )
                                embed1.set_image(url=(message.attachments[0].url))
                                await channel.send(embed=embed1)
        #This logs message edits and sends logs to Florida Control Room
        @commands.Cog.listener()
        async def on_message_edit(self, before, after):
                if before.guild.id == 504052021683290125:
                        channel = self.client.get_channel(643907825986306058) #message-edits channel in Florida Control Room
                        if before.content != after.content:
                                embed = discord.Embed(
                                colour = 0xff0000
                                )
                                embed.set_author(name=(before.author), icon_url=(before.author.avatar_url))
                                embed.add_field(name=f'Message was edited in #{before.channel}', value=(before.content),inline=False)
                                embed.add_field(name='Message now:', value=(after.content), inline=False)
                                embed.set_footer(text=(time.ctime()))
        
                                await channel.send(embed=embed)

        #This is the welcoming function. Sends welcomes to Florida, #welcome
        @commands.Cog.listener()
        async def on_member_join(self, member, invite = discord.Invite):
                if member.guild.id == 504052021683290125:
                        #These are the channels, FL = Florida, FCR = Control Room
                        channel = self.client.get_channel(507030960756228108) #Welcome, FL
                        channel3 = self.client.get_channel(643908037718966292) #joins channel, FCR
                        channel2 = self.client.get_channel(643915842865856524) #Members channel, FL

                        #This updates the member count in FCR
                        await channel2.edit(name= f'Members: {member.guild.member_count} ')

                        #This sends the welcome #message in FL
                        rules = self.client.get_channel(511614286640971796) # rules channel
                        await channel.send(f'Welcome to Florida {member.mention}! Make sure to read {rules.mention}!')

                        #This sends the message in #joins in FCR 
                        embed = discord.Embed(
                        colour = 0xff0000
                        )                
                        embed.set_author(name=f'{member} has joined the server')
                        embed.set_thumbnail(url=(member.avatar_url))
                        embed.set_footer(text=(time.ctime()))
                        await channel3.send(embed=embed)

                        #This checks if some has been gulag'd (role persist)
                        db = sqlite3.connect('main.sqlite')
                        cursor = db.cursor()
                        cursor.execute(f'SELECT user_id FROM gulag where user_id ={member.id}')
                        result = cursor.fetchone()

                        if result is not None:
                                role = discord.utils.get(member.guild.roles, name='Gulag\'d')
                                await member.add_roles(role)
                        else:
                                await asyncio.sleep(0.01)

                        await self.client.process_commands(member)

        #This is the message logging function in FCR
        @commands.Cog.listener()
        async def on_message(self, message):
                if message.guild.id == 504052021683290125:
                        channel = self.client.get_channel(643907801604948018)
                        if not message.author.id == 618903054506393640:
                                if not message.channel.id == 512429920912408576:
                                        if not message.attachments:
                                                embed = discord.Embed(
                                                colour = 0xff0000
                                                )                
                                                embed.set_author(name=(message.author), icon_url=(message.author.avatar_url))
                                                embed.add_field(name=f'{message.channel}', value=(message.content),inline=False)
                                                embed.set_footer(text=(time.ctime()))   
                                                #Message-Logs channel in FCR
                                                await channel.send(embed=embed)           
                                        else:
                                                embed1 = discord.Embed(
                                                colour = 0xff0000
 
                                                )
                                                embed1.set_image(url=(message.attachments[0].url))
                                                await channel.send(embed=embed1)

def setup(client):
        client.add_cog(Example(client))
