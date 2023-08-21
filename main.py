import discord

from helpers import get_env

intents = discord.Intents.default()
intents.message_content = True

DISCORD_TOKEN = get_env('DISCORD_TOKEN')
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} is the new mate in the room!')
    for guild in client.guilds:
        print(f'{client.user} is connected to the following guild:\n' + f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
	print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
	if message.author == client.user:
		return
	await message.channel.send(f'Hello, {message.author.name}!')

client.run(DISCORD_TOKEN)
