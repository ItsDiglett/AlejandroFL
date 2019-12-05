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
                    role = ctx.guild.get_role(512018933134524430)
                    await member.remove_roles(role)
                    await ctx.message.add_reaction('✅')
                    
                    sql = (f'DELETE FROM gulag WHERE user_id = {member.id}')
                    cursor.execute(sql)
                    db.commit()
                    #Baby Alejandro
                    bot = await self.client.fetch_user(618903054506393640)
                    #Mod-Actions Channel in FCR
                    channel = self.client.get_channel(643908781452820490)
                    message = ctx.message
                    
                    embed = discord.Embed(
                    colour = 0xff0000
                    )
                    embed.set_author(name=f'{ctx.message.author} has ungulaged {member}')
                    embed.set_thumbnail(url=(member.avatar_url))
                    embed.set_footer(text=f'{bot}• {time.ctime()}', icon_url=(bot.avatar_url))
                    
                    await channel.send(embed=embed)
                else:
                    await ctx.send('You don\'t have the permissions to use that command')

        @commands.command(pass_context=True,name='gulag', help='Gulags a member')
        async def gulag(self,ctx, member: discord.Member):
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT user_id FROM gulag where user_id ={member.id}')
            result = cursor.fetchone()
            #Baby Alejandro
            bot = await self.client.fetch_user(618903054506393640)
            #Mod-actions chat in FCR.
            channel = self.client.get_channel(643908781452820490)

            if result is None:
                if ctx.message.author.guild_permissions.manage_messages:
                    role = ctx.guild.get_role(512018933134524430)
                    await member.add_roles(role)
                    sql = ('INSERT INTO gulag(user_id, random) VALUES(?,?)')
                    val = (member.id, 1)
                    cursor.execute(sql, val)
                    db.commit()

                    embed = discord.Embed(
                    colour = 0xff0000
                    )
                    embed.set_author(name=f'{ctx.message.author} has gulaged {member}')
                    embed.set_thumbnail(url=(member.avatar_url))
                    embed.set_footer(text=f'{bot}• {time.ctime()}', icon_url=(bot.avatar_url))
                    await channel.send(embed=embed)
                    await ctx.message.add_reaction('✅')
                else:
                    await ctx.send('You can\'t use that command.')
            else:
                await asyncio.sleep(0.01)
                print('yes')

        @commands.command(pass_context=True,name='ban', help='Bans a member')
        async def ban(self, ctx, member : discord.Member, *, reason=None):
            if ctx.message.author.guild_permissions.manage_messages:
                await member.ban(reason = reason)
                await ctx.message.add_reaction('✅')
                #Mod-actions chat in FCR.
                channel = self.client.get_channel(643908781452820490)
                #Baby Alejandro
                bot = await self.client.fetch_user(618903054506393640)

                embed = discord.Embed(
                colour = 0xff0000
                )
                embed.set_author(name=(f'{ctx.message.author} has banned {member}.'))
                embed.set_thumbnail(url=(member.avatar_url))
                embed.set_footer(text=f'{bot}• {time.ctime()}', icon_url=(bot.avatar_url))
                await channel.send(embed=embed)
            else:
                await ctx.send('You don\'t have the permissions to use that command')

        @commands.command(pass_context=True, name='purge', help = 'purges messages from the chat.')
        async def purge(self, ctx, amount=5):
            if ctx.message.author.guild_permissions.manage_messages:
                await ctx.channel.purge(limit=amount)

            else:
                await ctx.send('You don\'t have the permissions to use that command.')

        @commands.command(pass_context=True,name='kick', help='Kicks a Member')
        async def kick(self, ctx, member : discord.Member, *, reason=None):
            if ctx.message.author.guild_permissions.manage_messages:
                await member.kick(reason=reason)
                await ctx.message.add_reaction('✅')
                #Mod-Actions Channel in FCR
                channel = self.client.get_channel(643908781452820490)
                #Baby Alejandro 
                bot = await self.client.fetch_user(618903054506393640)
                embed = discord.Embed(
                colour = 0xff0000
                )
                embed.set_author(name=(f'{ctx.message.author} has kicked {member}.'))
                embed.set_thumbnail(url=(member.avatar_url))
                embed.set_footer(text=f'{bot}• {time.ctime()}', icon_url=(bot.avatar_url))
                await channel.send(embed=embed)
            else:
                await ctx.send('You don\'t have the permissions to use that command')

        @commands.command()
        async def give(self, ctx, member:discord.Member, role):
            #Mod-Actions Channel in FCR
            channel = self.client.get_channel(643908781452820490)
            #Baby Alejandro
            bot = await self.client.fetch_user(618903054506393640)
            if ctx.message.author.guild_permissions.manage_messages:
                test = discord.utils.get(ctx.guild.roles, name=role)
                await member.add_roles(test)
                await ctx.message.add_reaction('✅')
                embed = discord.Embed(
                colour = 0xff0000
                )
                embed.set_author(name=(f'{ctx.message.author} has given {member} the {test} role'))
                embed.set_thumbnail(url=(member.avatar_url))
                embed.set_footer(text=f'{bot}• {time.ctime()}', icon_url=(bot.avatar_url))
                
                await channel.send(embed=embed)
            else:
                return
                          
def setup(client):
        client.add_cog(Moderation(client))