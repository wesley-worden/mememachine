import discord
import glob
import re

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
    #print(memefiles)
    #split into chunks
    chunksize = 50
    chunks = [memefiles[i:i + chunksize] for i in range(0, len(memefiles), chunksize)]
    #print(chunks)
    for memefileschunk in chunks:
        mememessage = "\n".join(memefileschunk)
        await message.author.send(mememessage)
    await message.channel.send("Boi i have slid into your dms with a list of memes")


async def handlemessage(message):
    if message.content.startswith('##list'):
        await listmemes(message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('##'):
        await handlemessage(message)

    if message.content.startswith("$hello"):
        await message.channel.send("goodbye.")

api_key_file = open("api-key","r")
api_key = api_key_file.readline()
api_key_file.close()

client.run(api_key)
