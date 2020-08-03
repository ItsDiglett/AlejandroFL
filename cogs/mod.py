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


vc = None

class Moderation(commands.Cog):
        def __init__(self,client):
                self.client=client
    
        @commands.command(pass_context=True,name='ungulag', help='Ungulags a member')
        async def ungulag(self, ctx, member: discord.Member, *, reasons=None):
            if ctx.message.author.guild_permissions.manage_messages:
                role = ctx.guild.get_role(Constants.GULAGED)
                db = sqlite3.connect('main.sqlite')
                cursor = db.cursor()
                cursor.execute(f'SELECT user_id FROM gulag where user_id ={member.id}')
                result = cursor.fetchone()
                if result is None:
                    await member.remove_roles(role)
                    await ctx.message.add_reaction('✅')
                else:
                    #Gulaged Role
                    await member.remove_roles(role)
                    await ctx.message.add_reaction('✅')
                    await Log.modlogs(self, ctx, mod=(ctx.message.author), action='ungulaged', members=(member), picture=(member.avatar_url), Grole=None, reason=reasons)
                    
                    sql = (f'DELETE FROM gulag WHERE user_id = {member.id}')
                    cursor.execute(sql)
                    db.commit()

        @commands.command(pass_context=True,name='gulag', help='Gulags a member')
        async def gulag(self,ctx, member: discord.Member, *, reasons=None):
            if ctx.message.author.guild_permissions.manage_messages:
                role = ctx.guild.get_role(Constants.GULAGED) #gulaged role
                nsfw = ctx.guild.get_role(Constants.NSFW)
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
                        await Log.modlogs(self, ctx, mod=(ctx.message.author), action='gulaged', members=(member), picture=(member.avatar_url), Grole=None, reason=reasons)
                        await Modactions.actionLogger(self, mod=(ctx.message.author), action='Gulaged', members=member.id, reason=reasons)
                        if nsfw in member.roles:
                            await member.remove_roles(nsfw)
                    else:
                        pass
                else:
                    await member.add_roles(role)
                    await ctx.message.add_reaction('✅')

            else: 
                pass

        @commands.command(pass_context=True,name='ban', help='Bans a member')
        async def ban(self, ctx, member : discord.Member, *, reasons=None):
            if ctx.message.author.guild_permissions.manage_messages:          
                await member.ban(reason=None, delete_message_days=0)
                await ctx.message.add_reaction('✅')
                await Log.modlogs(self, ctx, mod=(ctx.message.author), action='banned', members=(member), picture=(member.avatar_url), Grole=None, reason=reasons)
                await Modactions.actionLogger(self, mod=(ctx.message.author), action='Banned', members=member.id, reason=reasons)
            elif ctx.message.author.id == 618897651026493441:
                await member.ban(reason = reasons)
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
                await member.kick(reason=reasons)
                await ctx.message.add_reaction('✅')
                await Log.modlogs(self, ctx, mod=(ctx.message.author), action='kicked', members=(member), picture=(member.avatar_url), Grole=None, reason=reasons)
                await Modactions.actionLogger(self, mod=(ctx.message.author), action='Kicked', members=member.id, reason=reasons)
            else:
                pass

        
def setup(client):
        client.add_cog(Moderation(client))