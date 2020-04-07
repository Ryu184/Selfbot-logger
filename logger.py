import discord, asyncio
from os import system
import os
import os.path
from os import path

client = discord.Client()

token = ""

@client.event
async def on_message(message):
        wd=""
        if path.exists(wd+str(message.guild)):
            os.chdir(wd+str(message.guild))
        else:
            os.mkdir(wd+str(message.guild))
        File_object = open("log"+" - "+str(message.channel),"a")
        str1=str(message.author) + " "
        str2=str(message.created_at) + "\n"
        str3=str(message.guild) + " "
        str4=str(message.channel) + "\n"
        str5=message.content + "\n"
        L=[str1,str2,str3,str4,str5,"\n"]
        print(L)
        File_object.writelines(L)
client.run(token, bot=False)
