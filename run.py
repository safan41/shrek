import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
link = ["http://knowyourmeme.com/memes/", ]
TOKEN = 'NDU0MDE3ODIwODUwOTEzMjg4.Dfnk9A._L7ChlbseOleX9vp-9ISUDCamvs'

client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!meme'):
        mymsg = message.content[len('!meme'):].strip()
        link.append(mymsg)
        s = ''.join(link)
        page = urlopen(s)
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find('section', attrs={'class': 'bodycopy'})
        text = name_box.text.strip()
        await client.send_message(message.channel, s)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
