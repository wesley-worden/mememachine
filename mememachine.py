import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

api_key_file = open("api-key","r")
api_key = api_key_file.readline()
api_key_file.close()

client.run(api_key)
