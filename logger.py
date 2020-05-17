import discord, asyncio
from os import system
import os
from os import path
import sqlite3

client = discord.Client()
token = ""
wd=os.getcwd()

conn=sqlite3.connect('DiscordLog.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Discord(Guild TEXT,Channel TEXT,Author TEXT,Date TEXT,Message TEXT)")
@client.event
async def on_message(message):
        if not path.exists(wd+str(message.guild)):
            os.mkdir(wd+str(message.guild))
        gd=wd+str(message.guild)+'/'
        File_object = open(gd+"log - "+str(message.channel),"a")
        str1=str(message.author)
        str2=str(message.created_at)
        str3=str(message.guild)
        str4=str(message.channel)
        str5=message.content
        c.execute("INSERT INTO Discord(Guild,Channel,Author,Date,Message)VALUES (?,?,?,?,?)",(str3,str4,str1,str2,str5))
        conn.commit()
        L=[str1 + " ",str2 + "\n",str3 + " ",str4 + "\n",str5 + "\n","\n"]
        print(L)
        File_object.writelines(L)
        for attachment in message.attachments:
            if not path.exists(gd+"attachments/"):
                os.mkdir(gd+"attachments/")
            await attachment.save(gd+"attachments/"+attachment.filename)
client.run(token, bot=False)

