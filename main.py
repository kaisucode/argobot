
import discord
import asyncio
from urllib.request import urlopen
from bs4 import BeautifulSoup

TOKEN = '_YOUR_TOKEN_HERE_'
defaultChannel = discord.Object(id="440912837708218390")
client = discord.Client()


async def crawlAllSites(): 
    await client.send_message(defaultChannel, "Crawling all sites for changes")
    while(True): 
        await client.send_message(defaultChannel, "Hi, this is sent automatically")
        await asyncio.sleep(3)

@client.event
async def crawlSite(url): 
    print("Start crawling website url: \"" + url + "\"")

    #  html = open("supreme.html", "r").read()
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    soup.prettify()

    mainSite = "https://www.supremenewyork.com"

    for article in soup.findAll('article'):
        isSoldOut = article.findAll("div", {"class": "sold_out_tag"})
        if isSoldOut: 
            #  print("Sold out")
            continue

        embed = discord.Embed(title="Tile", description="Desc", color=0x00ff00)

        for a in article.findAll('a', href=True): 
            print(a['href'])
            embed.add_field(name="link", value=(mainSite+a['href']), inline=False)
        for img in article.findAll('img'): 
            print(img['src'])
            embed.set_image(url="https:"+img['src'])


        await client.send_message(defaultChannel, embed=embed)
    return
    
@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + "\n------")
    #  await crawlAllSites();
        

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message)
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}, this is argoBot'.format(message)
        print(message)
        print(message.channel)
        await client.send_message(message.channel, msg)

    elif message.content == "!supremeNY": 
        await crawlSite("https://www.supremenewyork.com/shop/all")


client.run(TOKEN)


