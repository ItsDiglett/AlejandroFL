import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime


class Log:
    def __init__(self, client, mod, action, members, picture, Grole):
        self.client=client
        self.mod =mod
        self.action =action
        self.members =members
        self.picture = picture
        self.Grole = Grole

    async def modlogs(self, ctx, mod, action, members, picture, Grole):
        if Grole == None:
            bot = await self.client.fetch_user(618903054506393640)
            channel = self.client.get_channel(643908781452820490)
            embed = discord.Embed(
            colour = 0xff0000
            )
            embed.set_author(name = f'{mod} has {action} {members}')
            embed.set_thumbnail(url=(picture))
            embed.set_footer(text=f'{bot}', icon_url=(bot.avatar_url))
            embed.timestamp = datetime.utcnow()
            
            await channel.send(embed=embed)
        else:
            bot = await self.client.fetch_user(618903054506393640)
            channel = self.client.get_channel(643908781452820490)
            embed = discord.Embed(
            colour = 0xff0000
            )
            embed.set_author(name = f'{mod} has {action} {members} {Grole}')
            embed.set_thumbnail(url=(picture))
            embed.set_footer(text=f'{bot}', icon_url=(bot.avatar_url))
            embed.timestamp = datetime.utcnow()

            await channel.send(embed=embed)

class MessageLog:
    def __init__(self, client, messages, members, picture, messagechannel, Mchannel):
        self.client = client
        self.messages = messages
        self.members = members
        self.picture = picture
        self.messagechannel = messagechannel
        self.Mchannel = Mchannel

    async def messagelogging(self, messages, members, picture, messagechannel, Mchannel):
        bot = await self.client.fetch_user(618903054506393640)
        channel = self.client.get_channel(Mchannel) #MessageLogs in FCR
        embed = discord.Embed(
        colour = 0xff0000
        )
        embed.set_author(name=(members), icon_url=(picture))
        embed.add_field(name=(messagechannel), value=(messages))
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f'{bot}', icon_url=(bot.avatar_url))

        await channel.send(embed=embed)
        
class EventLog:
    def __init__(self, client, event, picture, Mchannel):
        self.client = client
        self.event = event
        self.picture = picture
        self.Mchannel = Mchannel

    async def logevent(self, client, event, picture, Mchannel):
        bot = await self.client.fetch_user(618903054506393640)
        channel = self.client.get_channel(Mchannel)
        embed = discord.Embed(
        colour = 0xff0000
        )
        embed.set_author(name=(event))
        embed.set_thumbnail(url=(picture))
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f'{bot}', icon_url=(bot.avatar_url))

        await channel.send(embed=embed)
