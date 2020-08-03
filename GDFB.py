import discord
from discord.ext import commands
import os
from config import alejandro
import os
from discord.ext import commands
from config import alejandro
import random
import sqlite3
import Constants

print(os.getcwd())
client = commands.Bot(command_prefix='/')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def birthday(ctx):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.send(ctx.guild.created_at)

@client.command()
async def troll(ctx):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.send(f'The gods have chosen {(random.choice(ctx.guild.members).mention)}.')

@client.command()
async def facts(ctx, member: discord.Member):
    role = ctx.guild.get_role(737342687413403648)
    if ctx.message.author.guild_permissions.manage_messages:
        if len(role.members) >= 1:
            for members in role.members:
                await members.remove_roles(role)
                await member.add_roles(role)
        else:
            await member.add_roles(role)

@client.command()
async def invite(ctx):
        inivte = await ctx.channel.create_invite(reason=None, max_age=86400,max_uses=1)
        await ctx.message.author.send('This is a one time invite link that expires in 1 day.')
        await ctx.message.author.send(f'{inivte.url}')



client.run(Constants.AlEJANDROKEY)
