import discord
from urllib.request import urlopen
import re
import os
import praw
from discord.ext import commands
import computer
import time, random
import meme as me
import wolframalpha
# discord.py>=0.16.12
def remove_trash(index: list) -> list:
    if not isinstance(index, list):
        raise TypeError
    index.remove(index[0])
    index.remove(index[1])
    index.remove(index[2])
    try:
        for i in range(39, 116):
            index.remove(index[i])
    except IndexError:
        pass
listotrash = ["pickles", "stars", "potatoes", "fs", "hundred million thousand stars"]
single = ["pickle", "star", "potato", "f", "hundred million thousand stars"]
reddit = praw.Reddit(client_id='FvsbeaJuTBqqvA',
                     client_secret='730UrhjmPn3qwp_4STdnVk7l2K0',
                     password='maryhadalittlelamb',
                     user_agent='testscript by /u/fakebot3',
                     username='pabloitoman')
client = discord.Client()
wolf = wolframalpha.Client(os.environ['WOLFRAM'])
bot = commands.Bot(command_prefix='?', description='A bot that greets the user back.')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Shrek meme bot thing", description="Very bot. So much nice. List of commands are:", color=0x33bd33)

    embed.add_field(name="?hello", value="Gives a nice greet message", inline=False)
    embed.add_field(name="?meme <meme>", value="Returns given meme information from knowyourmeme.com", inline=False)
    embed.add_field(name="?memereview <literally anything>", value="Returns a rating of anything basically", inline=False)
    embed.add_field(name="?ping", value="Returns ping", inline=False)
    embed.add_field(name="?compute <expression>", value="Solves simple Maths", inline=False)
    embed.add_field(name="?help", value="Gives this message", inline=False)
    embed.add_field(name="?top <subreddit>", value="Takes given subreddit and returns top of all time", inline=False)
    embed.add_field(name="?hot <subreddit>", value="Takes given subreddit and returns hot", inline=False)

    await ctx.send(embed=embed)
    await ctx.send("Any additional support for this bot can be found at @safan41#9134 and @ithinknotdumbo#5355's discord server: https://discord.gg/BAnCs4E")
@bot.command()
async def hello(ctx):
    await ctx.send('Hello {0.author.mention}'.format(ctx))

@bot.command()
async def peepee(ctx):
    await ctx.send('poopoo man')

@bot.command()
async def ping(ctx):
    await ctx.send(" :ping_pong: Pong! Ping: {}ms".format(round(bot.latency * 1000)))

@bot.command()
async def pls(self, ctx, *, message: str):
    text_channel = await commands.TextChannelConverter.convert(ctx, message)
    msg = '{0.author.mention}\nPlease move this to {1.mention}'.format(ctx, text_channel)
    await ctx.send(msg)


@bot.command()
async def compute(ctx, *, exp: str):
    try:
        await ctx.send("That equals" + str(computer.NumericStringParser.eval(exp[0])))
    except:
        await ctx.send("Couldn't parse" + exp + " maybe check for proper signs/formatting?")

@bot.command()
async def memereview(ctx, *message: str):
    if not message:
        await ctx.send("I need a meme to review")
    else:
        stars = random.randint(0, 5)
        if stars == 0:
            listotrash.remove("hundred million thousand stars")
            trash = random.choice(listotrash)
        elif stars == 1:
            trash = random.choice(single)
        else:
            trash = random.choice(listotrash)
        await ctx.send("I'd rate this meme to be " + str(stars) + " " + str(trash) + " :ok_hand:")
        if stars == 0:
            listotrash.append("hundred million thousand stars")

@bot.command()
async def top(ctx, *, message: str):
    try:
        hot = reddit.subreddit(message).top('all')
        linkd = []
        thelink = []
        finlink = []
        for sub in hot:
            linkd.append(sub.shortlink)
        for id in linkd:
            if linkd.index(id) <= 10:
                thelink.append(id + "\n")
        sh = ''.join(thelink)
        finlink.append(sh)
        shs = ''.join(finlink)
        mgs = "Here's what's top of ALL TIME on r/" + message +":\n" + shs
        await ctx.send(mgs)   
    except:
        await ctx.send("The subreddit r/" + message + " doesn't exist.")
@top.error
async def top_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a subreddit")

@bot.command()
async def hot(ctx, *, message: str):
    try:
        hot = reddit.subreddit(message).hot()
        linkd = []
        thelink = []
        finlink = []
        for sub in hot:
            linkd.append(sub.shortlink)
        for id in linkd:
            if linkd.index(id) <= 10:
                thelink.append(id + "\n")
        sh = ''.join(thelink)
        finlink.append(sh)
        shs = ''.join(finlink)
        mgs = "Here's what's top of ALL TIME on r/" + message +":\n" + shs
        await ctx.send(mgs)   
    except:
        await ctx.send("The subreddit r/" + message + " doesn't exist.")
@hot.error
async def hot_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a subreddit")

@bot.command()
async def meme(ctx, *, message: str):
    link = ["https://knowyourmeme.com/memes/"]
    link.append(message)
    s = ''.join(link)
    data = me.getMemeData(s)
    embed = discord.Embed(title=data.get("name"), color=0x33bd33)
    embed.set_thumbnail(url=data.get("photo"))
    try:
        embed.add_field(name="Status", value=data.get("status"), inline=False)
    except:
        pass
    try:
        embed.add_field(name="Type", value=data.get("type"), inline=False)
    except:
        pass
    try:
        embed.add_field(name="Origin Year", value=data.get("origin_year"), inline=False)
    except:
        pass
    try:
        embed.add_field(name="Origin Place", value=data.get("origin_place"), inline=False)
    except:
        pass
    try: 
        embed.add_field(name="About", value=data.get("about"), inline=False)
    except:
        pass
    try:
        embed.add_field(name="Origin", value=data.get("origin"), inline=False)
    except:
        pass
    
    await ctx.send(embed=embed)

@meme.error
async def meme_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a meme")

@bot.command()
async def alpha(ctx, *, message: str):
    try:
        res = wolf.query(message)
        await ctx.send(next(res.results).text)   
    except:
        await ctx.send("The requested query couldn't be parsed. Please make sure your query makes sense")
@alpha.error
async def alpha_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add a query")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
bot.run(os.environ['TOKEN'])
# await client.send_message(message.channel, 'Error - No meme stats found for "' + mymsg + '"') if anything goes worng