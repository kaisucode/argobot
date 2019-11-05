
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup


def crawlSite(url): 
    print("Start crawling website url: \"" + url + "\"")

    defaultChannel = discord.Object(id="440912837708218390")
    client = discord.Client()

    html = open("supreme.html", "r").read()
    #  html = urlopen(url).read()
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


        client.send_message(defaultChannel, embed=embed)


#  crawlSite("https://www.supremenewyork.com/shop/all")

