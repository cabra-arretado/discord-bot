import discord

from helpers import get_env

intents = discord.Intents.default()
# intents.message_content = True

DISCORD_TOKEN = get_env('DISCORD_TOKEN')
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is the new mate in the room!')

client.run(DISCORD_TOKEN)
