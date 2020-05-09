import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

#commonly used values
prefix = "##"
#status = "potatoe.exe"

#helper functions
def getapikey():
    api_key_file = open("api-key", "r")
    api_key = api_key_file.readline()
    api_key_file.close()
    return api_key

#async def messagehim(text):
#    await bot.send_message(discord.Object(id=
#print("*begins screeching*")
#end helper functions

#begin bot, actual things start to happen here
print("*begins screeching*")
#write process pid to die file
if os.path.exists("idontwannadie"): #if die file exists
    os.remove("idontwannadie") #destroy it
fout = open("idontwannadie", "wt")
fout.write(str(os.getpid()))
print(os.getpid())
fout.close()
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
#    await bot.change_presence(game=discord.Game(name=status))
    print("bruh we made it " + bot.user.name)
#    await messagehim("MemeMachine up and running like a dream bruh")

#commands
@bot.command(brief="returns the id for your user bruh", description="bruh")
async def getid(context):
    message = context.message
    await message.author.send(str(message.author.id))
#end commands

@bot.event
async def on_message(message):
    #ignore messages from muh' self
    if message.author == bot.user:
        return

    #process commands
    await bot.process_commands(message)

bot.run(getapikey(), bot=True)
