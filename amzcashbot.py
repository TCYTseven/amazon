import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents)



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Legit Invite Rewards!'))
    print('Bot Online!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def invite(ctx):
    await ctx.send("__**Invite The Bot Here:**__, https://discord.com/api/oauth2/authorize?client_id=834045666246262824&permissions=8&scope=bot")

@client.command()
async def kind(ctx):
    await ctx.send("Be Kind!")


@client.command(aliases =['8ball'])
async def _8ball(ctx, *, question):
    responces = ['It is certain.',
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now."]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responces)}')

@client.command()
async def roast(ctx, *, user):
    responses = ['Wow, your maker really didn’t waste time giving you a personality, huh?',
                "I’m an acquired taste. If you don’t like me, acquire some taste.:sunglasses:",
                'Oh. you don’t like being treated the way you treat me? That must suck.',
                "I’m busy right now; can I ignore you another time?",
                "I'm a human not a mirror :clown:",
                "zombies eat brains so your safe :wink:",
                "Light travels faster than sound, which is why you seemed bright until you spoke.",
                "You have an entire life to be an idiot. Why not take today off?"]

    await ctx.send(f'Roasting User: {user}\nGet Rect: {random.choice(responses)}')


@client.command(aliases = ['purge'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Purged", amount, "Messages!")

@client.command()
async def userinfo(ctx):
    user = ctx.author
    embed=discord.Embed(title="USER INFO", description=f"Here is the info we retrieved about {user}", colour=user.colour)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="NAME", value=user.name, inline=True)
    embed.add_field(name="NICKNAME", value=user.nick, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
    await ctx.send(embed=embed)







@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} was kicked!")

client.run('ODM0Mzk4NzMwMTQ0NDQ4NTY0.YIAUXw._FG2SfrumFOtjVm0Zf2lQdXA_ro')
