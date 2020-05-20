import sqlite3
from datetime import datetime
import discord
from discord.ext import commands
from discord.utils import get
import Constants

class Modactions:
    def __init__(self, mod, action, members):
        self.mod = mod
        self.action = action
        self.members = members
        
    async def actionLogger(self, mod, action,members, reason):
        now = datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f'Select reason FROM logs WHERE user_id={members}')
        sql = ('INSERT INTO logs(user_id, reason) VALUES(?,?)')
        val = (members, f'{date_string}: {action} by {mod} | Reason: {reason}')
        cursor.execute(sql, val)
        db.commit()

    

class database:
    def __init__(self, user, Mchannel, thumbnail):
        self.user = user
        self.channel = Mchannel
        self.thumbnail = thumbnail

    async def opendb(self, user, Mchannel, thumbnail):
        #This gets the XP
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f'SELECT msg FROM messages WHERE user_id = {user}')
        result = cursor.fetchone()

        #This gets the index
        db1 = sqlite3.connect('main.sqlite')
        cursor1 = db1.cursor()
        cursor1.execute(f'SELECT user_id FROM messages ORDER BY msg DESC')
        result2 = cursor1.fetchall()
        #This gets the true rank
        spot = result2.index((f'{user}',))
        truespot = spot + 1

        channel = self.client.get_channel(Mchannel)
        mention = await self.client.fetch_user(user)
        
        embed = discord.Embed(
        colour = Constants.ROLE_COLOUR
        )
        embed.set_author(name=(mention))
        embed.set_thumbnail(url=(thumbnail))
        embed.add_field(name=f'Rank: {truespot}', value=f'{result[0]}xp')
        
        await channel.send(embed=embed)
