import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime


class Log:
    def __init__(self, client, mod, action, members, Grole):
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
    def __init__(self, client, messages,after, members, picture, messagechannel):
        self.client = client
        self.messages = messages
        self.after = after
        self.members = members
        self.picture = picture
        self.messagechannel = messagechannel

    async def messageedits(self,client,messages, after, members, picture, messagechannel):
        bot = await self.client.fetch_user(618903054506393640)
        channel = self.client.get_channel(643907825986306058) #MessageEdits in FCR
        embed = discord.Embed(
        colour = 0xff0000
        )
        embed.set_author(name=(members), icon_url=(picture))
        embed.description = f'**Message was edited in** {messagechannel}'
        embed.add_field(name='Before', value=(messages), inline=False)
        embed.add_field(name='After:', value=(after), inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f'{bot}', icon_url=(bot.avatar_url))

        await channel.send(embed=embed)



    async def messages(self, messages, members, picture, messagechannel):
        bot = await self.client.fetch_user(618903054506393640)
        channel = self.client.get_channel(643907801604948018) #MessageLogs in FCR
        embed = discord.Embed(
        colour = 0xff0000
        )
        embed.set_author(name=(members), icon_url=(picture))
        embed.add_field(name=(messagechannel), value=(messages))
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f'{bot}', icon_url=(bot.avatar_url))

        await channel.send(embed=embed)

    async def deletes(self, messages, members, picture, messagechannel):
        bot = await self.client.fetch_user(618903054506393640)
        channel = self.client.get_channel(643907846651772948) #MessageDeletes in FCR
        embed = discord.Embed(
        colour = 0xff0000
        )
        embed.set_author(name=(members), icon_url=(picture))
        embed.add_field(name=f'Message was deleted in #{messagechannel}', value=(messages), inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f'{bot}', icon_url=(bot.avatar_url))

        await channel.send(embed=embed)
