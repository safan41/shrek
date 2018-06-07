import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
link = ["http://knowyourmeme.com/memes/", ]
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
        msgg = "Available commands: \n !hello - says hello back \n !meme - goes on KnowYourMeme to see requested meme's stats".format(message)
        await client.send_message(message.channel, msgg)
    if message.content.startswith('!meme'):
        mymsg = message.content[len('!meme'):].strip()
        link.append(mymsg)
        s = ''.join(link)
        power = []
        try:
            page = urlopen(s)
            soup = BeautifulSoup(page, 'html.parser')
            name_box = soup.find_all('p')
            for i in name_box:
                power.append(i.get_text)
            #v = ''.join(power)
            await client.send_message(message.channel, "Find out more at " + s)
            remove_trash(power)
        except:
            await client.send_message(message.channel, 'Error - No meme stats found for "' + mymsg + '"')
@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + " (" + client.user.id + ")")
    print("Testing commands:")
    print('------')

client.run(TOKEN)
# await client.send_message(message.channel, 'Error - No meme stats found for "' + mymsg + '"') if anything goes worng