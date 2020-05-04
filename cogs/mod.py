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
from embedcreator import Log
from actions import Modactions

vc = None

class Moderation(commands.Cog):
        def __init__(self,client):
                self.client=client
    
        @commands.command(pass_context=True,name='ungulag', help='Ungulags a member')
        async def ungulag(self, ctx, member: discord.Member):
            if ctx.message.author.guild_permissions.manage_messages:
                role = ctx.guild.get_role(512018933134524430)
                db = sqlite3.connect('main.sqlite')
                cursor = db.cursor()
                cursor.execute(f'SELECT user_id FROM gulag where user_id ={member.id}')
                result = cursor.fetchone()
                if result is None:
                    await member.remove_roles(role)
                    await ctx.message.add_reaciton('✅')
                else:
                    #Gulaged Role
                    await member.remove_roles(role)
                    await ctx.message.add_reaction('✅')
                    await Log.modlogs(self, ctx, mod=(ctx.message.author), action='ungulaged', members=(member), picture=(member.avatar_url), Grole=None)
                    
                    sql = (f'DELETE FROM gulag WHERE user_id = {member.id}')
                    cursor.execute(sql)
                    db.commit()

        @commands.command(pass_context=True,name='gulag', help='Gulags a member')
        async def gulag(self,ctx, member: discord.Member, *, reasons=None):
            role = ctx.guild.get_role(512018933134524430) #gulaged role
            nsfw = ctx.guild.get_role(512421686587424768)
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT user_id FROM gulag where user_id ={member.id}')
            result = cursor.fetchone()
            if result is None:
                if ctx.message.author.guild_permissions.manage_messages:               
                    await member.add_roles(role)
                    sql = ('INSERT INTO gulag(user_id, random) VALUES(?,?)')
                    val = (member.id, 1)
                    cursor.execute(sql, val)
                    db.commit()
                    await ctx.message.add_reaction('✅')
                    await Log.modlogs(self, ctx, mod=(ctx.message.author), action='gulaged', members=(member), picture=(member.avatar_url), Grole=None)
                    await Modactions.actionLogger(self, mod=(ctx.message.author), action='Gulaged', members=member.id, reason=reasons)
                    if nsfw in member.roles:
                        await member.remove_roles(nsfw)
                else:
                    pass
            else:
                await member.add_roles(role)
                await ctx.message.add_reaction('✅')

        @commands.command(pass_context=True,name='ban', help='Bans a member')
        async def ban(self, ctx, member : discord.Member, *, reasons=None):
            if ctx.message.author.guild_permissions.manage_messages:          
                await member.ban(reason = reason)
                await ctx.message.add_reaction('✅')
                await Log.modlogs(self, ctx, mod=(ctx.message.author), action='banned', members=(member), picture=(member.avatar_url), Grole=None)
                await Modactions.actionLogger(self, mod=(ctx.message.author), action='Banned', members=member.id, reason=reasons)
            elif ctx.message.author.id == 618897651026493441:
                await member.ban(reason = reason)
            else:
                pass

        @commands.command(pass_context=True, name='purge', help = 'purges messages from the chat.')
        async def purge(self, ctx, amount=5):
            if ctx.message.author.guild_permissions.manage_messages:
                await ctx.channel.purge(limit=amount)
            else:
                pass

        @commands.command(pass_context=True,name='kick', help='Kicks a Member')
        async def kick(self, ctx, member : discord.Member, *, reasons=None):
            if ctx.message.author.guild_permissions.manage_messages:
                await member.kick(reason=reason)
                await ctx.message.add_reaction('✅')
                await Log.modlogs(self, ctx, mod=(ctx.message.author), action='kicked', members=(member), picture=(member.avatar_url), Grole=None)
                await Modactions.actionLogger(self, mod=(ctx.message.author), action='Kicked', members=member.id, reason=reasons)
            else:
                pass
        @commands.command(pass_context=True,name='trust', help='Gives a member the Publix Customer role')
        async def trust(self, ctx, member: discord.Member):
            if ctx.message.author.guild_permissions.manage_messages:
                role = ctx.guild.get_role(573544311132520469) #Trusted role or whatever Matt wants to call it
                await member.add_roles(role)
                await ctx.message.add_reaction('✅')
                await Log.modlogs(self, ctx, mod=(ctx.message.author), action='trusted', members=(member), picture=(member.avatar_url), Grole=None)
            else:
                pass

        @commands.command(pass_context=True,name='give', help='Gives a member a role')
        async def give(self, ctx, member:discord.Member, role):
            if ctx.message.author.guild_permissions.manage_messages:
                test = discord.utils.get(ctx.guild.roles, name=role)
                await member.add_roles(test)
                await ctx.message.add_reaction('✅')
                await Log.modlogs(self, ctx, mod=(ctx.message.author), action='given', members=(member), picture=(member.avatar_url), Grole=str(test))
                
            else:
                return

        @commands.command(pass_context=True,name='verify', help='Locks the verify channel')
        async def verify(self, ctx):
            if ctx.message.author.guild_permissions.manage_messages:
                unverified = ctx.guild.get_role(671074340636459008) #Unverified Role
                channel = self.client.get_channel(511614286640971796) #Rules-And-Verify Channel
                await channel.set_permissions(unverified, read_messages=False)

        @commands.command(pass_context=True,name='unverify', help='unlocks the verify channel')
        async def unverify(self, ctx):
            if ctx.message.author.guild_permissions.manage_messages:
                unverified = ctx.guild.get_role(671074340636459008) #Unverified Role
                channel = self.client.get_channel(511614286640971796) #Rules-And-Verify Channel
                await channel.set_permissions(unverified, read_messages=True)

        @commands.command(pass_context=True,name='slowmode', help='Sets the channel to slowmode')
        async def slowmode(self, ctx):
            if ctx.message.author.guild_permissions.manage_messages:
                channel = ctx.message.channel
                if channel.slowmode_delay == 0:                      
                    await channel.edit(slowmode_delay=15)
                else:
                    await channel.edit(slowmode_delay=0)

        @commands.command(pass_context=True, name='t', help = 'Text to speech')
        async def t(self, ctx, *, texts:str):
            global vc
            if ctx.message.author.guild_permissions.manage_messages:
                tts = gtts.gTTS(texts)
                tts.save("tts.mp3")
                channel = ctx.message.author.voice.channel
                if vc is None:
                    vc = await channel.connect()
                elif vc.channel != channel:
                    vc = await channel.connect()  

                vc.play(discord.FFmpegPCMAudio(f'tts.mp3')) 
                while vc.is_playing():
                        await asyncio.sleep(0.1)
                vc.stop()
            else:
                pass

        @commands.command(pass_context=True, name='leave', help = 'forces Alejandro out of VC')
        async def leave(self,ctx):
            server = ctx.message.guild.voice_client
            await server.disconnect()           

        @commands.command()
        async def info(self, ctx, member: discord.Member):
            if ctx.message.author.guild_permissions.manage_messages:
                db = sqlite3.connect('main.sqlite')
                cursor = db.cursor()
                cursor.execute(f'Select reason FROM logs WHERE user_id={member.id}')
                result = cursor.fetchall()
                if result is None:
                    await ctx.send('This user has no history of moderation.')
                else:

                    embed = discord.Embed(
                    colour = 0xb3f0f3
                    )
                    embed.set_author(name=(member), icon_url=(member.avatar_url))
                    embed.title = '__Moderation Logs__'
                    embed.add_field(name='Actions:', value='\n'.join([str(i[0])for i in result]), inline=False)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    channel = ctx.message.channel

                    await channel.send(embed=embed)
            else:
                pass


def setup(client):
        client.add_cog(Moderation(client))