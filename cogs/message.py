import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import os
import time
import sqlite3
import math
import random
from actions import database

class leaderboard(commands.Cog):
        def __init__(self,client):
                self.client=client
        
        @commands.Cog.listener()
        async def on_message(self, message):
            #Xp Database
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT msg FROM messages WHERE user_id = {message.author.id}')
            result = cursor.fetchone()
            #If your not in the database, this adds you
            if result is None:
                sql = ('INSERT INTO messages(user_id, MSG) VALUES(?,?)')
                rand1 = random.randint(15, 25)
                val = (message.author.id, rand1)
                cursor.execute(sql, val)
                db.commit()
            else:
                #This makes sure Baby Alejandro(the bot) doesn't get xp
                if message.author.id == 618903054506393640:
                    pass
                #This gives you XP if you are already in the database
                else:
                    cursor.execute(f'SELECT msg FROM messages WHERE user_id = {message.author.id}')
                    result1 = cursor.fetchone()
                    msg = int(result1[0])
                    sql = ('UPDATE messages SET msg = ? WHERE user_id = ?')
                    rand = random.randint(15, 25)
                    val = (msg + rand, str(message.author.id))
                    cursor.execute(sql, val)
                    db.commit()

                    #cursor.execute(f'SELECT seasonxp FROM messages WHERE user_id ={message.author.id}')
                    #result2 = cursor.fetchone()
                    #xp = int(result2[0])
                    #print(xp)
                    #sql = ('UPDATE messages SET seasonxp = ? WHERE user_id = ?')
                    #val = (xp + rand, str(message.author.id))
                    #cursor.execute(sql, val)
                    #db.commit()


        @commands.command(name='rank', help='shows a members rank')
        async def rank(self, ctx, user:discord.User = None):
            #If there is no @mention in the rank command
            if user is None:
                await database.opendb(self, user=(ctx.message.author.id), Mchannel=(ctx.message.channel.id), thumbnail=(ctx.message.author.avatar_url))
            #If there is an @mention in the rank command
            if user is not None:
                await database.opendb(self, user=(user.id), Mchannel=(ctx.message.channel.id), thumbnail=(user.avatar_url))

        #This displays the leaderboard. It's terribly done, I know. I'll fix it later.
        @commands.command(name='leaderboard', help='shows the server leaderboard')
        async def leaderboard(self, ctx):
            db = sqlite3.connect('main.sqlite')
            db.row_factory = lambda cursor, row: row[0]
            cursor = db.cursor()
            cursor1 = db.cursor()
            cursor1.execute(f'SELECT msg FROM messages ORDER BY msg DESC')
            cursor.execute(f'Select user_id FROM messages ORDER BY msg DESC')
            results1 = cursor1.fetchall()
            result = cursor.fetchall()
            print(result[1])
            t1 = await self.client.fetch_user(result[0])
            t2 = await self.client.fetch_user(result[1])
            t3 = await self.client.fetch_user(result[2])
            t4 = await self.client.fetch_user(result[3])
            t5 = await self.client.fetch_user(result[4])
            t6 = await self.client.fetch_user(result[5])
            t7 = await self.client.fetch_user(result[6])
            t8 = await self.client.fetch_user(result[7])
            t9 = await self.client.fetch_user(result[8])
            t10 = await self.client.fetch_user(result[9])

            channel = ctx.message.channel
            embed = discord.Embed(
            colour = discord.Colour.blue()
            )
            embed.add_field(name=f'Users:', value=f'1. {t1}\n2. {t2}\n3. {t3}\n4. {t4}\n5. {t5}\n6. {t6}\n7. {t7}\n8. {t8}\n9. {t9}\n10. {t10}\n\nDon\'t see your name? Do /rank to find out your XP!', inline=True)
            embed.set_author(name= 'Florida Leader Board', icon_url=(ctx.guild.icon_url))
            embed.add_field(name=f'Scores:', value=f'{results1[0]}\n{results1[1]}\n{results1[2]}\n{results1[3]}\n{results1[4]}\n{results1[5]}\n{results1[6]}\n{results1[7]}\n{results1[8]}\n{results1[9]}')
            
            await channel.send(embed=embed)



                

def setup(client):
        client.add_cog(leaderboard(client))