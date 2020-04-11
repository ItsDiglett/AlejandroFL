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


class Moderation(commands.Cog):
        def __init__(self,client):
                self.client=client

        @commands.command(pass_context=True,name='ungulag', help='Ungulags a member')
        async def ungulag(self, ctx, member: discord.Member):

            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT user_id FROM gulag where user_id ={member.id}')
            result = cursor.fetchone()
            if result is None:
                await asyncio.sleep(0.01)
            else:
                if ctx.message.author.guild_permissions.manage_messages:           
                    role = ctx.guild.get_role(512018933134524430) #Gulaged Role
                    await member.remove_roles(role)
                    await ctx.message.add_reaction('✅')
                    await Log.modlogs(self, ctx, mod=(ctx.message.author), action='ungulaged', members=(member), picture=(member.avatar_url), Grole=None)
                    
                    sql = (f'DELETE FROM gulag WHERE user_id = {member.id}')
                    cursor.execute(sql)
                    db.commit()
                else:
                    pass

        @commands.command(pass_context=True,name='gulag', help='Gulags a member')
        async def gulag(self,ctx, member: discord.Member):

            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT user_id FROM gulag where user_id ={member.id}')
            result = cursor.fetchone()
            if result is None:
                if ctx.message.author.guild_permissions.manage_messages:
                    role = ctx.guild.get_role(512018933134524430) #Gulaged Role
                    NSFW = ctx.guild.get_role(512421686587424768) #NSFW Role
                    await member.add_roles(role)
                    sql = ('INSERT INTO gulag(user_id, random) VALUES(?,?)')
                    val = (member.id, 1)
                    cursor.execute(sql, val)
                    db.commit()

                    await ctx.message.add_reaction('✅')
                    await Log.modlogs(self, ctx, mod=(ctx.message.author), action='gulaged', members=(member), picture=(member.avatar_url), Grole=None)
                else:
                    pass
            else:
                await asyncio.sleep(0.01)
                print('yes')

        @commands.command(pass_context=True,name='ban', help='Bans a member')
        async def ban(self, ctx, member : discord.Member, *, reason=None):
            if ctx.message.author.guild_permissions.manage_messages:          
                await member.ban(reason = reason)
                await ctx.message.add_reaction('✅')
                await Log.modlogs(self, ctx, mod=(ctx.message.author), action='banned', members=(member), picture=(member.avatar_url), Grole=None)
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
        async def kick(self, ctx, member : discord.Member, *, reason=None):
            if ctx.message.author.guild_permissions.manage_messages:
                await member.kick(reason=reason)
                await ctx.message.add_reaction('✅')
                await Log.modlogs(self, ctx, mod=(ctx.message.author), action='kicked', members=(member), picture=(member.avatar_url), Grole=None)
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

        @commands.command()
        async def t(self, ctx, *, texts:str):
            global vc
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

        @commands.command()
        async def vote(self, ctx, *question:str):
            if ctx.message.author.guild_permissions.manage_messages:
                embed = discord.Embed(
                colour = 0xff0000
                )

                embed.title = ' '.join(question)
                embed.add_field(name='Options:', value='✅Yes \n🚫No')
                embed.timestamp = datetime.utcnow()

                channel = ctx.message.channel
                message = await channel.send(embed=embed)
                await message.add_reaction('✅')
                await message.add_reaction('🚫')

        @commands.command()
        async def leave(self, ctx):
            server = ctx.message.guild.voice_client
            await server.disconnect()    



def setup(client):
        client.add_cog(Moderation(client))