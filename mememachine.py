import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import glob

#commonly used values
prefix = "##"
#status = "potatoe.exe"

#helper functions
def getapikey():
    api_key_file = open("api-key", "r")
    api_key = api_key_file.readline()
    api_key_file.close()
    return api_key

def findmemes(query, numresults):
    memefiles = getmemefiles()
    matches = [k for k in memefiles if query in k]
    return matches[:numresults]

def getmemefiles():
    memefiles = []
    for file in glob.glob("muh_sounds_bruh/**/*.flac", recursive=True):
            file = file[len("muh_sounds_bruh/"):]
            file = file[:-(len(".flac"))]
            memefiles.append(file)
    memefiles.sort()
    return memefiles 

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
    print("bruh we made it " + bot.user.name + "#" + bot.user.discriminator)
#    await messagehim("MemeMachine up and running like a dream bruh")

#commands
@bot.command(brief="plays the requested meme bruh", description="will play the meme in muh sounds bruh that exactly matches")
async def play(context, meme=""):
    message = context.message
    if not meme:
        await message.channel.send("bruh i need a meme to play")
        return
    meme = findmemes(meme, 1)[0]
    if(meme == []):
        await message.channel.send("no meme bruh")
    else:
        memepath = "/home/pepesilvia/mememachine/muh_sounds_bruh/" + meme + ".flac"
        await message.channel.send("i wanna play " + memepath)


@bot.command(brief="returns the integer id for your user bruh", description="returns the integer id for your user bruh, useful for discord debug n shit")
async def getid(context):
    message = context.message
    await message.author.send(str(message.author.id))

@bot.command(brief="search and find up to 25 memes bruh", description="shows the first 25 memes that contain substrings that exactly match bruh")
async def search(context, query=""):
    message = context.message
    if not query:
        await message.channel.send("try using a search term bruh")
        return
    matches = findmemes(query, 25)
    if(matches == []):
        await message.channel.send("no sounds bruh")
    else:
        matches.insert(0, "")
        searchmessage = "\n".join(matches)
        await message.channel.send("bruh are you lookin for ```" + searchmessage + "```") 

@bot.command(brief="sends you all the memes in a massive DM, dont", description="this will tear into your DMs and send you all the available memes, which is so many memes bro. to actually send all the memes use\n##list memes\nthis is done to prevent your destruction")
async def list(context, password=""):
    message = context.message
    if not password:
        await message.channel.send("bruh i am so full of memes, if you are sure you want this use `##list memes`")
        return
    elif(password == "memes"):
        await message.author.send("here are the available memes:")
        memefiles = getmemefiles()
        #split into chunks
        chunksize = 50
        chunks = [memefiles[i:i + chunksize] for i in range(0, len(memefiles), chunksize)]
        for memefileschunk in chunks:
            mememessage = "\n".join(memefileschunk)
            await message.author.send(mememessage)
        await message.channel.send("you will not survive")
#end commands

@bot.event
async def on_message(message):
    #ignore messages from muh' self
    if message.author == bot.user:
        return
    if message.content.startswith("##help"):
        await message.channel.send("_\"My guess is that you've been confused for a very long time.\"_")

    #process commands
    await bot.process_commands(message)

bot.run(getapikey(), bot=True)
