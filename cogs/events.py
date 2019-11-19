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
                if message.guild.id == 504052021683290125:
                        channel = self.client.get_channel(643907846651772948) #message-deletes in Florida Control room
                        embed = discord.Embed(
                        colour = 0xff0000
                        )
                        embed.set_author(name=(message.author), icon_url=(message.author.avatar_url))
                        embed.add_field(name=(f'Message was deleted'), value=(message.content), inline=False)
                        embed.set_footer(text=(time.ctime()))

                        await channel.send(embed=embed)

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

        #This checks if you've been saying the n-word.
        @commands.Cog.listener()
        async def on_message(self, message):
                badword = json.loads(open('nwords.json').read())
                for badwords in badword:
                        #This is the list of badwords, stored in a .json file
                        if badwords in message.content:
                                db = sqlite3.connect('main.sqlite')
                                cursor = db.cursor()
                                cursor.execute(f'SELECT count FROM nword WHERE user_id = {message.author.id}')
                                result = cursor.fetchone()
                                #If you aren't in the database, it adds you
                                if result is None:
                                        sql = ('INSERT INTO nword(user_id, count) VALUES(?,?)')
                                        val = (message.author.id, 1)
                                        cursor.execute(sql, val)
                                        db.commit()
                                else:
                                        #If you are in the database, it adds a point.
                                        cursor.execute(f'SELECT count FROM nword WHERE user_id = {message.author.id}')
                                        result1 = cursor.fetchone()
                                        msg = int(result1[0])
                                        sql = ('UPDATE nword SET count = ? WHERE user_id = ?')
                                        val = (msg + 1, str(message.author.id))
                                        cursor.execute(sql, val)
                                        db.commit()
                        else:
                                await asyncio.sleep(0.001)

        #This is the message logging function in FCR
        @commands.Cog.listener()
        async def on_message(self, message):
                if message.guild.id == 504052021683290125:
                        if not message.author.id == 618903054506393640:
                                if not message.channel.id == 512429920912408576:
                                        embed = discord.Embed(
                                        colour = 0xff0000
                                        )                
                                        embed.set_author(name=(message.author), icon_url=(message.author.avatar_url))
                                        embed.add_field(name=f'{message.channel}', value=(message.content),inline=False)
                                        embed.set_footer(text=(time.ctime()))   
                                        #Message-Logs channel in FCR
                                        channel = self.client.get_channel(643907801604948018)

                                        await channel.send(embed=embed)           

def setup(client):
        client.add_cog(Example(client))
