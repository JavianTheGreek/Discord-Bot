import discord
from discord.ext import commands

# Import Token from discord..
discordPass = ''

# Commands prefic inwhich the bot responses to..
client = commands.Bot(command_prefix='!!')

@client.event
async def on_ready():
    print('The Bot is online has we speak....')


@client.event
async def on_message(msg):
    if msg.content.find('Hello') != -1:
        await msg.channel.send('Hi,')
    # Without this the code won't work...
    await client.process_commands(msg)
        

client.run(discordPass)
