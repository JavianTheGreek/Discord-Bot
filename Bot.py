import discord
from discord.ext import commands

# Import Token from discord..
discordPass = ''

# Commands prefix in which the bot responses to..
client = commands.Bot(command_prefix="!!")

i = open("rules.txt", "r")
rules = i.readlines()
# Put words in list you want to ban from server..
remove = ['Kill', 'kill', 'Anime is trash']  # Anime Goated no slandering..


@client.event
async def on_ready():
    print('The Bot is online has we speak....')


@client.event
async def on_message(msg):
    for line in remove:
        if line in msg.content:
            await msg.delete()
    await client.process_commands(msg)


@client.command(aliases=['rules', 'r'])
async def rule(txt, *, num):
    await txt.send(rules[int(num) - 1])


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(txt, amount=100):
    await txt.channel.purge(limit=amount)


@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(txt, member: discord.Member, *, reason="You Have been kicked"):
    await member.send("Reason for kicking." + reason)
    await member.kick(reason=reason)


@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(txt, member: discord.Member, *, reason="You Have been ban for a reason"):
    await txt.send(member.name + " You Have been Ban, " + reason)
    await member.ban(reason=reason)


@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(txt, *, member):
    banned_users = await txt.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_disc):
            await txt.guild.unban(user)
            await txt.send(member_name + " has been unbanned!!!!")
            return

    await txt.send(member + " was not found")


@client.command(aliases['m'])
@commands.has.permissons(kick_members=True)
async def mute(txt, member : discord.Member):
    muted_role = txt.guild(The muted role you created)
    
    await member.add_role(muted_role)
    await txt.send(member.mention + " Has been muted")
    
    
@client.command(aliases['um'])
@commands.has.permissons(kick_members=True)
async def unmute(txt, member : discord.Member):
    muted_role = txt.guild(The muted role you created)
    
    await member.remove.role(muted_role)
    await txt.send(member.mention + " Has been unmuted!!!!")
    
    
    
# client = BotClient()
client.run(discordPass)

