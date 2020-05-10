#import pdb
#print("press c and then enter if the next line runs just fine")
#pdb.set_trace()
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord import FFmpegPCMAudio
from discord.utils import get
import os
import glob
import aiohttp
import json
import asyncio
import random
#import giphy_client
#from giphy_client.rest import ApiException
#import signal
#import sys

#please shrek, we pray to you, watch over this bot
#let him play the memes for our bretheren and their defenenders,
#and to kill this bot if he betrays your legacy or his master
#def shrek_wrangler(shrek_is_love, shrek_is_life):
#    print("damn bruh giving me the hard Ctrl+C")
#    sys.exit(0)
#signal.signal(signal.SIGINT, shrek_wrangler)

#commonly used values
prefix = "##"
memepath = "/home/pepesilvia/mememachine/muh_sounds_bruh/dva-okay.flac"
#status = "potatoe.exe"
wednesday_channel = 708554699225301002

#global shit
playing = False
endsig = False
shrek_images = [ "http://churchofshrek.yolasite.com/resources/417930_240580199418458_792918923_n.jpg",
        "https://i.pinimg.com/564x/cf/8c/f4/cf8cf4528649708b8a022a3bc6cabb01.jpg",
        "https://i.pinimg.com/236x/24/55/94/245594470ed0704eba0c89654c0d0f57.jpg",
        "https://cdn.drawception.com/images/panels/2016/8-12/FMSKyT3j6O-2.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTG5-FXMKGyVzf6TJyCXrl4PQ35S6YSbAQcRoEt2QaMNdTAWqiV&s",
        "https://pbs.twimg.com/media/CxUhUibUcAAV-tQ.jpg",
        "https://i.chzbgr.com/full/9125133824/h1CBCE60B/funny-meme-about-shrek-and-worshiping-him" ]
shrek_words = [ "shrek", "love", "life", "donkey", "swamp", "god", "healer", "holy", "worship", "soul", "light",
        "redemption", "righteous" ] 

#get giphy key
giphy_key_file = open("giphy-key", "r")
giphy_key = giphy_key_file.readline()
giphy_key = giphy_key.rstrip('\r\n')
giphy_key_file.close()
#giphy_api_instance = giphy_client.DefaultApi()
session = aiohttp.ClientSession()


#set shreks holy code
print("*kneels in prayer*")
print("please shrek, we pray to you, watch over this bot")
print("let him play the memes for our bretheren and their defenenders,")
print("and to kill this bot if he betrays your legacy or his master")
random.shuffle(shrek_words)
shreks_holy_code = "".join(shrek_words[:4])
print("\n our holy god answers: " + shreks_holy_code)

#helper functions
def getrandomshrekimage():
    return random.choice(shrek_images)

def getapikey():
    api_key_file = open("api-key", "r")
    api_key = api_key_file.readline()
    api_key_file.close()
    return api_key


def findmemes(query, numresults):
    memefiles = getmemefiles()
    matches = [k for k in memefiles if query in k]
    matches.sort()
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
pid = os.getpid()
print("muh' pid is " + str(pid))
fout = open("idontwannadie", "wt")
fout.write(str(pid))
fout.close()
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
#    await bot.change_presence(game=discord.Game(name=status))
    print("bruh we made it we " + bot.user.name + "#" + bot.user.discriminator)
#    await messagehim("MemeMachine up and running like a dream bruh")

#commands
#@tasks.loop(seconds=1.0)
#async def playerender(context, player):
#    global endsig
#    global playing
#    if(endsig == True):
#        print("killing player")
#        player.stop()
#        endsig = False
#        playing = False
#        self.playerender.cancel()

#@tasks.loop(seconds=0.1)
#a#sync def memeplayer(context, memepath, channel):
 #   global playing
 #   global endsig
 #   if(playing == True):
 #       print("blocking, sending endsig")
 #       endsig = True
 #   while(playing == True):
 #       print("waiting...")
 #       pass
 #   print("done/no more waiting...")
 #   endsig = True
 #   #done playing other memes
 #   #switch voice channels if needed
 #   voice = get(bot.voice_clients, guild=context.guild)
 #   if voice and voice.is_connected():
 #       await voice.move_to(channel)
 #   else:
 #       voice = await channel.connect()
 #   print("playing " + memepath)
 #   endsig = False
 #   playing = True
 #   source = FFmpegPCMAudio(memepath)
async def playerhelper(voice, source):
    player = voice.play(source)
 #   while voice.is_playing() == True:
 #       if endsig == True:
 #           player.stop()
 #           print("stopped by endsig")
 #           endsig = False
 #           playing = False
 #   playing = False
 #   player.stop()
 #   print("stopped")
 #   #disconnect when done
 #   #await voice.disconnect()
 #   memeplayer.cancel()

source = FFmpegPCMAudio(memepath)
#player = voice.play(source)
player: discord.VoiceClient
playing = False
task = None
@bot.command()
async def cancel(context, *args):
    global task
    task.cancel()

@bot.command(brief="plays the requested meme bruh", description="will play the meme in muh sounds bruh that exactly matches")
async def play(context, *args):
    global playing
    #global endsig
    #global player
    #global memepath
    #global source
    global task
    message = context.message
    if not args:
        await message.channel.send("bruh i need a meme to play")
        return
    meme = args[0]
    #make sure we can access voice
    if not message.author.voice:
        await message.channel.send("bruh i am too dumb to access the voice channel because we are in the DMs, use #meme-machine in rowdys")
        return
    #check if they are in a voice channel first
    channel = context.message.author.voice.channel
    if(channel == None):
        await message.channel.send("bruh you gotta be in a voice channel first")
        return
    #find the meme
    memepath = "/home/pepesilvia/mememachine/muh_sounds_bruh/" + meme + ".flac"
    if not os.path.exists(memepath):
        meme = findmemes(meme, 1)[0]
        if(meme == []):
            await message.channel.send("no meme bruh")
            return
    memepath = "/home/pepesilvia/mememachine/muh_sounds_bruh/" + meme + ".flac"
    #await message.channel.send("i wanna play " + memepath)
    print("trying to spawn new memeplayer")
    #pdb.set_trace()
    #memeplayer.start(context, memepath, channel)
    if(playing == True):
        print("blocking:")
        task.cancel()
    if not task is None:
        print("canceling task")
        task.cancel()
    #print("waiting")
    #while(playing == True):
    #    pass
    #print("done waiting")
    #    #endsig = True
    #    player.close()
    #    playing = False
       # player.stop()
    #print("waiting...")
    #while(playing == True):
    #    pass
    #print("done/no more waiting...")
    #endsig = True
    #done playing other memes
    #switch voice channels if needed
    voice = get(bot.voice_clients, guild=context.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    print("playing " + memepath)
    #endsig = False
#    def my_after(error):
#        coro = message.channel.send("`" + meme + "` is over bruh")
#        fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
#        try:
#            fut.result()
#        except:
#            # an error happened sending the message
#            pass
#
    source = FFmpegPCMAudio(memepath)
    playing = True
    task = bot.loop.create_task(playerhelper(voice, source))
    #player = voice.play(source, after=my_after)
    #playerender.start(context, player)
    #while voice.is_playing() == True:
    #    if endsig == True:
    #        player.stop()
    #        print("stopped by endsig")
    #        endsig = False
    #        playing = False
    #playing = False
    #player.stop()
    #print("stopped")
    #disconnect when done
    #await voice.disconnect()

    
@bot.command()
async def gif(context, *args):
    message = context.message
    if not args:
        await message.channel.send("i _wont_ gif empty strings bruh")
        return
    query = args[0]
    query_url = args[0]
    for arg in args[1:]:
        query = query + " " + arg
        query_url = query_url + "%20" + arg
    request = "https://api.giphy.com/v1/gifs/search?api_key=" + giphy_key + "&q=" + query_url + "&limit=1&offset=0&rating=R&lang=en"
    response = await session.get(request)
    data = json.loads(await response.text())
    url = data['data'][0]['embed_url']
    #print(message.channel.id)
    memechannel = message.channel
    if type(memechannel) is discord.DMChannel:
        memechannel = bot.get_channel(wednesday_channel)
    await memechannel.send("`" + query + "`")
    await memechannel.send(url)

@bot.command(brief="kills me bruh pls dont", description="bruh pls bruh i dont wanna die bruh\nto kill me you have to use my pid found in the `idontwannadie` file or printed out when i was born\nnot for normies")
async def kys(context, *args):
    global session
    message = context.message
    if not args:
        await message.channel.send("you think you can kill me? normies cant kill me bruh you gotta use muh pid")
        return
    password = args[0]
    if password == str(pid):
        await message.channel.send("im sorry you feel that way bruh\n_*dies*_")
        print("recieved kill command, sepeku time")
        session.close()
        await bot.close()

@bot.command()
async def shreksmite(context, *args):
    global session
    message = context.message
    if not args:
        await message.channel.send("wut are yu doin in mah swamp?! how dare you try to summon shrek to smite me you filthy casual")
        return
    password = args[0]
    for arg in args[1:]:
        password = password + arg
    if password == shreks_holy_code:
        await message.channel.send(getrandomshrekimage())
        await message.channel.send("**its all ogre now**\n_*dies*_")
        print("recieved kill command, sepeku time")
        session.close()
        await bot.close()

@bot.command(brief="returns the integer id for your user bruh", description="returns the integer id for your user bruh, useful for discord debug n shit")
async def getid(context):
    message = context.message
    await message.channel.send(str(message.author.id))

#@bot.command(brief="search and find up to 25 memes bruh", description="shows the first 25 memes that contain substrings that exactly match bruh")
#async def search(context, *args):
#    message = context.message
#    if not args:
#        await context.channel.send("try using a search term bruh")
#        return
#    query = args[0]
#    matches = findmemes(query, 25)
#    matches.sort()
#    if(matches == []):
#        await message.channel.send("no sounds bruh")
#    else:
#        matches.insert(0, "")
#        searchmessage = "\n".join(matches)
#        await message.channel.send("bruh are you lookin for ```" + searchmessage + "```")

@bot.command(brief="search and find up to 25 memes bruh", description="shows the first 25 memes that contain substrings that exactly match bruh")
async def search(context, *args):
    message = context.message
    if not args:
        await context.channel.send("try using a search term bruh")
        return
    query = args[0]
    matches = findmemes(query, 500)
    matches.sort()
    if(matches == []):
        await message.channel.send("no sounds bruh")
    else:
        #matches.insert(0, "")
        #searchmessage = "\n".join(matches)
        #await message.channel.send("bruh are you lookin for ```" + searchmessage + "```")
        await message.channel.send("bruh are you lookin for")
        chunksize = 50
        chunks = [matches[i:i + chunksize] for i in range(0, len(matches), chunksize)]
        for matcheschunk in chunks:
            for string in matcheschunk:
                string.prepend("`")
                string.append("`")
            mememessage = "\n".join(matcheschunk)
            await message.channel.send(mememessage)

@bot.command(brief="sends you all the memes in a massive DM, dont", description="this will tear into your DMs and send you all the available memes, which is so many memes bro. to actually send all the memes use\n##list memes\nthis is done to prevent your destruction")
async def list(context, *args):
    message = context.message
    if not args or args[0] != "memes":
        await message.channel.send("bruh i am so full of memes, if you are sure you want this use `##list memes`")
        return
    await message.channel.send("you will not survive")
    await message.author.send("here are the available memes:")
    memefiles = getmemefiles()
    #split into chunks
    chunksize = 50
    chunks = [memefiles[i:i + chunksize] for i in range(0, len(memefiles), chunksize)]
    for memefileschunk in chunks:
        mememessage = "\n".join(memefileschunk)
        await message.author.send(mememessage)

@bot.command(brief="prints this message bruh", description="bruh dont you have something better to be doin")
async def help(context, *args):
    message = context.message
    message.channel.send("to be implemented bruh")
    #if not args:
    #    pass
    #    #print normal help message
    #    messages = []
    #    messages.append("available commands:")
    #    messages.append("`play meme` " + bot.commands.play.brief)
    #    await message.channel.send("\n".join(messages))
    #command = args[0]
    #print help message based on command
#end commands

@bot.event
async def on_message(message):
    #ignore messages from muh' self
    if message.author == bot.user:
        return
    #insert a cheeky lil quote if its the help message
    if message.content.startswith("##help"):
        await message.channel.send("_\"My guess is that you've been confused for a very long time.\"_")

    #other cheeky sayings
    if "weed" in message.content or "420" in message.content:
        await message.channel.send("ayy weed lmao")
    #process commands
    await bot.process_commands(message)

bot.run(getapikey(), bot=True)
