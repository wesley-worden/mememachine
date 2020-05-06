import discord
import glob
import re
import difflib

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def getmemefiles():
    memefiles = []
    for file in glob.glob("muh_sounds_bruh/**/*.flac", recursive=True):
            file = file[len("muh_sounds_bruh/"):]
            file = file[:-(len(".flac"))]
            memefiles.append(file)
    memefiles.sort()
    return memefiles


async def listmemes(message):
    await message.author.send("Here are the available memes:")
    memefiles = getmemefiles()
    #split into chunks
    chunksize = 50
    chunks = [memefiles[i:i + chunksize] for i in range(0, len(memefiles), chunksize)]
    for memefileschunk in chunks:
        mememessage = "\n".join(memefileschunk)
        await message.author.send(mememessage)
    await message.channel.send("Boi i have slid into your dms with a list of memes")

def findmemes(query, numresults):
    memefiles = getmemefiles()
    matches = [k for k in memefiles if query in k]
    print(matches)
    return matches[:numresults]

async def handlesearch(message):
    query = message.content[len("##search "):]
    matches = findmemes(query, 25)
    if(matches == []):
        await message.channel.send("no sounds bruh")
    else:
        matches.insert(0, "")
        searchmessage = "\n".join(matches)
        await message.channel.send("bruh are you lookin for ```" + searchmessage + "```")

async def handlemessage(message):
    if message.content.startswith("##search"):
        await handlesearch(message)
    if message.content.startswith('##list'):
        await listmemes(message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('##'):
        await handlemessage(message)

api_key_file = open("api-key","r")
api_key = api_key_file.readline()
api_key_file.close()

client.run(api_key)
