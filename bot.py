import discord
from urllib.request import urlopen
import re
import praw
from discord.ext import commands
import time
# discord.py>=0.16.12
link = ["http://knowyourmeme.com/memes/"]
TOKEN = 'NDU0MDE3ODIwODUwOTEzMjg4.Dfnk9A._L7ChlbseOleX9vp-9ISUDCamvs'
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
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!help'):
        msgg = "Available commands: \n !hello - says hello back \n !meme - goes on KnowYourMeme to see requested meme's stats \n !hot - goes on requested subreddit to retrieve 10 in category hot \n !top - goes on requested subreddit to retrieve 10 in category top of all time".format(message)
        await client.send_message(message.channel, msgg)
    if message.content.startswith('!meme'):
        mymsg = message.content[len('!meme'):].strip()
        if message.content[len('review')]:
            pass
        else:
            link.append(mymsg)
            s = ''.join(link)
            try:
                await client.send_message(message.channel, "Find out more at " + s)
                link.remove(mymsg)
            except:
                await client.send_message(message.channel, 'Error - No meme stats found for "' + mymsg + '"')
    if message.content.startswith('!despacito2'):
        msgg = "Will... \n never happen :ok_hand:".format(message)
        await client.send_message(message.channel, msgg)
    if message.content.startswith('!memereview'):
        mymsg = message.content[len('!memereview'):].strip()
        import random
        stars = random.randint(0, 5)
        if stars == 0:
            listotrash.remove("hundred million thousand stars")
            trash = random.choice(listotrash)
        elif stars == 1:
            trash = random.choice(single)
        else:
            trash = random.choice(listotrash)
        await client.send_message(message.channel, "I'd rate this meme to be " + str(stars) + " " + str(trash) + " :ok_hand:")
        if stars == 0:
            listotrash.append("hundred million thousand stars")
    if message.content.startswith('!hot'):
        mymsgs = message.content[len('!hot'):].strip()
        try:
            hot = list(reddit.subreddit(mymsgs).hot())
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
            mgs = "Here's what's hot on r/" + mymsgs +":\n" + shs
            await client.send_message(message.channel, mgs)   
        except:
            await client.send_message(message.channel, "The subreddit r/" + mymsgs + " doesn't exist.")
    if message.content.startswith('!top'):
        mymsgsg = message.content[len('!top'):].strip()
        try:
            hot = list(reddit.subreddit(mymsgsg).top('all'))
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
            mgs = "Here's what's on the TOP of all time on r/" + mymsgsg +":\n" + shs
            await client.send_message(message.channel, mgs)   
        except:
            await client.send_message(message.channel, "The subreddit r/" + mymsgsg + " doesn't exist.")

    if message.content.startswith("!ping"):
        """pseudo-ping time"""
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        await client.send_message(channel, " :ping_pong: Pong! Ping: {}ms".format(round((t2-t1)*1000)))
@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + " (" + client.user.id + ")")
    print("Testing commands:")
    print('------')
client.run(TOKEN)
# await client.send_message(message.channel, 'Error - No meme stats found for "' + mymsg + '"') if anything goes worng