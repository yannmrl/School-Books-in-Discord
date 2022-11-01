import discord
import requests
import asyncio
from pyppeteer import launch

client = discord.Client()

manuels = ['geo', 'histoire', 'maths', 'mathex', 'allemand', 'espagnol', 'physique', 'enseignement_sci', 'philo', 'anglais', 'mathcomp', 'svt']

async def webScreen(wPage,mess,manuel):
    browser = await launch()
    page = await browser.newPage()
    if manuel == 'allemand':
        await page.goto('https://exobank.hachette-livre.fr/contents/final/9782016290200-fxl/OEBPS/Page_'+wPage+'.html')
    elif manuel == 'histoire':
        if len(wPage) == 1:
            pageN = '00'+str(int(wPage)+2)
        elif len(wPage) == 2:
            pageN = '0'+str(int(wPage)+2)
        elif len(wPage) == 3:
            pageN = str(int(wPage)+2)
        await page.goto('https://storage.libmanuels.fr/Magnard/specimen/9782210114418/17/OEBPS/page'+pageN+'.xhtml')
    elif manuel == 'anglais':
        if len(wPage) == 1:
            pageN = '00'+str(int(wPage)+2)
        elif len(wPage) == 2:
            pageN = '0'+str(int(wPage)+2)
        elif len(wPage) == 3:
            pageN = str(int(wPage)+2)
        await page.goto('https://storage.libmanuels.fr/Magnard/specimen/9782210114029/19/OEBPS/page'+pageN+'.xhtml')
    elif manuel == 'geographie':
        if len(wPage) == 1:
            pageN = '00'+str(int(wPage)+2)
        elif len(wPage) == 2:
            pageN = '0'+str(int(wPage)+2)
        elif len(wPage) == 3:
            pageN = str(int(wPage)+2)
        await page.goto('https://storage.libmanuels.fr/Magnard/specimen/9782210114357/12/OEBPS/page'+pageN+'.xhtml')
    await page.screenshot({'path': 'assets/manuels.jpg', 'fullPage': 'true'})
    await browser.close()
    await mess.channel.send(file=discord.File('assets/manuels.jpg'))

@client.event
async def on_ready():
    print("ready client 1")

@client.event
async def on_message(message):
    if not "discriminator='5746'" in str(message):
        if "!manuel" in message.content:
            args = message.content.split(" ")
            if any(x in args for x in manuels):
                if args[1] == 'physique':
                    f = open('assets/manuels.jpg', 'wb')
                    response = requests.get('https://p.calameoassets.com/200831152507-99c183a66adc7dae17d836461cf5556d/p' + str(int(args[2]) + 2) + '.jpg')
                    f.write(response.content)
                    f.close()
                    await message.channel.send(file=discord.File('assets/manuels.jpg'))
                elif args[1] == 'mathex':
                    f = open('assets/manuels.jpg', 'wb')
                    response = requests.get('https://p.calameoassets.com/200831152507-99c183a66adc7dae17d836461cf5556d/p' + str(int(args[2]) + 2) + '.jpg')
                    f.write(response.content)
                    f.close()
                    await message.channel.send(file=discord.File('assets/manuels.jpg'))
                elif args[1] == 'philo':
                    f = open('assets/manuels.jpg', 'wb')
                    response = requests.get('https://p.calameoassets.com/200330171613-ca326a0db0cd16d4028669b383f69453/p' + str(int(args[2]) + 2) + '.jpg')
                    f.write(response.content)
                    f.close()
                    await message.channel.send(file=discord.File('assets/manuels.jpg'))
                elif args[1] == 'allemand':
                    await webScreen(args[2], message, 'philo')
                elif args[1] == 'enseignement_sci':
                    f = open('assets/manuels.jpg', 'wb')
                    response = requests.get('https://www.editions-hatier.fr/flip/flex/docs/e/9782401063211/9782401063211.pdf_'+str(int(args[2])+2) + '.jpg?d=20210912162304')
                    f.write(response.content)
                    f.close()
                    await message.channel.send(file=discord.File('assets/manuels.jpg'))
                elif args[1] == 'anglais':
                    await webScreen(args[2], message, 'anglais')
                elif args[1] == 'histoire':
                    await webScreen(args[2], message, 'histoire')
                elif args[1] == 'geo':
                    await webScreen(args[2], message, 'geographie')
                elif args[1] == 'mathcomp':
                    f = open('assets/manuels.jpg', 'wb')
                    response = requests.get('https://p.calameoassets.com/200330174931-420cc2621af55a58bedd200ce12b09e7/p' + str(int(args[2]) + 2) + '.jpg')
                    f.write(response.content)
                    f.close()
                    await message.channel.send(file=discord.File('assets/manuels.jpg'))
                elif args[1] == 'svt':
                    f = open('assets/manuels.jpg', 'wb')
                    response = requests.get('https://p.calameoassets.com/200421182207-cc60de80f877a8f3d00e6c06545e142d/p' + str(int(args[2]) + 18) + '.jpg')
                    f.write(response.content)
                    f.close()
                    await message.channel.send(file=discord.File('assets/manuels.jpg'))
            else:
                await message.channel.send('il existe pas ce manuel, voici la liste des manuels disponibles : '+manuels[0]+', '+manuels[1]+', '+manuels[2]+', '+manuels[3]+', '+manuels[4]+', '+manuels[5]+', '+manuels[6]+', '+manuels[7]+', '+manuels[8]+', '+manuels[9])

client.run("XXXXXXXXXXXXXXXXXXX.XXXXX.XXXXXXXXXXXX_XXXX")