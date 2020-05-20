import discord
from discord.ext import commands
from embedcreator import MessageLog, EventLog
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import os
import json
import time
import sqlite3
from datetime import datetime, timedelta
import Constants

class Example(commands.Cog):
        def __init__(self,client):
                self.client=client

        @commands.Cog.listener()
        async def on_ready(self):
                print('It\'s alive!')
                
        #This is logs the message deletes. Sends Logs to Florida Control Room
        @commands.Cog.listener()
        async def on_message_delete(self, message = discord.Message):                
                if message.guild.id == Constants.FLORIDA:                
                        await MessageLog.messagelogging(self, messages=(message.content), members=(message.author), picture=(message.author.avatar_url), messagechannel=f'Message was deleted in #{message.channel}:', Mchannel=Constants.DELETES)
        #This logs message edits and sends logs to Florida Control Room
        @commands.Cog.listener()
        async def on_message_edit(self, before, after):
                if before.guild.id == Constants.FLORIDA:
                        if before.content != after.content:
                                await MessageLog.messagelogging(self, messages=f'**Before:**\n{before.content}\n**After:**\n{after.content}',members=(before.author), picture=before.author.avatar_url, messagechannel=(before.channel), Mchannel=Constants.EDITS)

        #This is the welcoming function. Sends welcomes to Florida, #welcome
        @commands.Cog.listener()
        async def on_member_join(self, member, invite = discord.Invite):
                if member.guild.id == Constants.FLORIDA:
                        unverified = member.guild.get_role(671074340636459008)
                        await member.add_roles(unverified)
                        
                        channel = self.client.get_channel(Constants.WELCOME)
                        channel2 = self.client.get_channel(Constants.MEMBERS)
                        
                        #This updates the member count in FCR
                        await channel2.edit(name= f'Members: {member.guild.member_count} ')
                        #This sends the welcome #message in FL
                        rules = self.client.get_channel(Constants.RULESVERIFY)
                        await channel.send(f'Welcome to Florida {member.mention}! Make sure to read {rules.mention}!')

                        #This sends the message in #joins in FCR 
                        await EventLog.logevent(self, self.client, event=f'{member} has joined the server', picture=(member.avatar_url), Mchannel=Constants.JOINS)
                        #This checks if some has been gulag'd (role persist)
                        db = sqlite3.connect('main.sqlite')
                        cursor = db.cursor()
                        cursor.execute(f'SELECT user_id FROM gulag where user_id ={member.id}')
                        result = cursor.fetchone()

                        if result is not None:
                                role = discord.utils.get(member.guild.roles, name='Gulaged')
                                await member.add_roles(role)
                        else:
                                await asyncio.sleep(0.01)

                        await self.client.process_commands(member)

        @commands.Cog.listener()
        async def on_member_remove(self, member):
                if member.guild.id == Constants.florida:
                        channel = self.client.get_channel(Constants.MEMBERS) #members channel
                        await EventLog.logevent(self, self.client, event=f'{member} has left the server', picture=(member.avatar_url), Mchannel= Constants.LEAVES)
                        await channel.edit(name= f'Members: {member.guild.member_count} ')
                else:
                        pass

                await self.client.process_commands(member)

        #This is the message logging function in FCR
        @commands.Cog.listener()
        async def on_message(self, message):
                if message.guild.id == Constants.FLORIDA:
                        if not message.author.id == 618903054506393640:
                                if not message.channel.id == 512429920912408576:
                                        await MessageLog.messagelogging(self, messages=(message.content),members=(message.author),picture=(message.author.avatar_url), messagechannel=(message.channel), Mchannel= Constants.MESSAGELOGS)

        @commands.Cog.listener()
        async def on_voice_state_update(self, member, before, after):
                if not before.channel and after.channel:
                        await EventLog.logevent(self, self.client, event=f'{member} has joined {after.channel}(VC)', picture=(member.avatar_url), Mchannel=Constants.VCLOGS)

                elif before.channel and not after.channel:
                        await EventLog.logevent(self, self.client, event=f'{member} has left {before.channel}(VC)', picture=(member.avatar_url), Mchannel=Constants.VCLOGS)     

                elif not before.mute and after.mute:
                        await EventLog.logevent(self, self.client, event=f'{member} has been muted.', picture=(member.avatar_url), Mchannel=Constants.VCLOGS)

                elif not before.deaf and after.deaf:
                        await EventLog.logevent(self, self.client, event=f'{member} has been deafened.', picture=(member.avatar_url), Mchannel=Constants.VCLOGS)

def setup(client):
        client.add_cog(Example(client))
