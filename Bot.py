import discord
from discord.ext import commands

# Import Token from discord..
discordPass = 'NjE4MjA2MTY1OTY4NDg2NTc3.XW2TWw.KdMmfU49EZoHpxVRmDpTxZYj3to'

# Commands prefic inwhich the bot responses to..
client = commands.Bot(command_prefix='x')

@client.event
async def on_ready():
    print('The Bot is online has we speak....')
@client.event
async def on_message(msg):
    if msg.content.find('xhello') != -1:
        await msg.channel.send('Wassup G')

client.run(discordPass)