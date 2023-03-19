import requests
import random
import secrets
import discord
import asyncio
from time import sleep

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

opentoken = open("token.txt", 'r')
TOKEN = opentoken.read()

laused = 'laused.txt'

kaheksaball = "8ball.txt"

nool = 'nool.txt'

rest_chan = 'rest_chan.txt'




@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    rest_channels = open(rest_chan, 'r+')
    restricted_channels = rest_channels.read().splitlines()
    print(restricted_channels)
    rest_channels.close()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$math'):
        await message.channel.send('mathing:nerd:')
        sleep(2)
        message_content = message.content
        mesg_con = message_content.replace('$math ', '')
        if mesg_con == "me+yourmom":
            tehe = "yourdad"
        elif mesg_con == "me+your mom":
            tehe = "your dad"
        else:
            tehe = eval(mesg_con)
        tehet = (str(mesg_con) + "=" + str(tehe))
        print(tehet)
        await message.channel.send(tehet)
    elif message.content.startswith('$score'):
        file = 'scoor.txt'
        openscoor = open(file,"r+")
        scoor = openscoor.read()
        openscoor.close()
        openscore = open(file,"w+")
        mesag_con = message.content.replace('$score ', '')
        openscore.write(str(int(scoor) + int(mesag_con)))
        openscore.close()
        opnscr = open(file,"r+")
        score = opnscr.read()
        await message.channel.send(score)
        opnscr.close()
        scoor = ''
    elif message.content.startswith('$meth'):
        await message.channel.send('mething :100:')
        sleep(1)
        await message.channel.send(':100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100:')
    elif message.content.startswith('$nitrogen'):
        await message.channel.send("*generating free nitro*")
        nitro = message.content.replace('$nitrogen ', '')
        def gen_gift(length):
            return secrets.token_hex(length // 2)
        
        
        for j in range(int(nitro)):
            for i in range(50):
                GIFT_CODE = ('discord.gift/' + gen_gift(16))
                
                response = requests.get(f'https://discord.com/api/v6/entitlements/gift-codes/{GIFT_CODE}', headers={'Authorization': f'Bot {TOKEN}'})
                # Check the status code of the response
                if response.status_code == 200:
                    # If the status code is 200, the gift code is valid
                    await message.channel.send('Gift code is valid:   ' + 'discord.gift/' + '{GIFT_CODE}')
                    break
            await message.channel.send("didn't find nitro")
            sleep(1)
    elif message.content.startswith('$nitrogen debug'):
        await message.channel.send("*generating free nitro*")
        nitro = message.content.replace('$nitrogen debug ', '')
        def gen_gift(length):
            return secrets.token_hex(length // 2)
        
        
        for j in range(int(nitro)):
            for i in range(50):
                GIFT_CODE = ('discord.gift/' + gen_gift(16))
                print(str(GIFT_CODE))
                response = requests.get(f'https://discord.com/api/v6/entitlements/gift-codes/{GIFT_CODE}', headers={'Authorization': f'Bot {TOKEN}'})

                # Check the status code of the response
                if response.status_code == 200:
                    # If the status code is 200, the gift code is valid
                    await message.channel.send('Gift code is valid:   ' + 'discord.gift/' + '{GIFT_CODE}')
                    break
            await message.channel.send("didn't find nitro")
            sleep(1)
    elif message.content.startswith('$addlause'):
        fail = open(laused, 'a')
        
        fail.write("""
"""+ message.content.replace('$addlause ', ''))
        
        fail.close()
        await message.channel.send('lause "' + message.content.replace('$addlause ', '') + '" on salvestatud')
    elif message.content.startswith("$8pall"):
        fileee = open(kaheksaball, 'r')
        lausee = fileee.read().splitlines()
        await message.channel.send(("Minu vastus sinu kusimusele '" + message.content.replace('$8pall ', '') + "' on: " + random.choice(lausee)))
        fileee.close()
    elif message.content.startswith("$nool"):
        fliec = open(nool, 'w')
        fliec.close()
        noolarv = message.content.replace('$nool ', '')
        for l in range(int(noolarv)):
            noollength = random.randint(1, 101)
            fileeee = open(nool, 'a+')
            for k in range(noollength):
                fileeee.write('-')
            fileeee.write(">")
            fileeee.close()
            fileeeee = open(nool, 'r')
            await message.channel.send(fileeeee.read())
            print(fileeeee.read())
            fileeee.close()
            filew = open(nool, 'w')
            filew.close()
    elif message.content.startswith("$help"):
        await message.channel.send("""Boti prefiks on $
Commandid:
nool - teeb kindla koguse nooli
nitrogen - proovib genereerida nitrot
math - lahendab tehte
meth - :skull:
8pall - see annab vastuse
score - lisab antud koguse skoori uleuldisesse skoori kogusesse
addlause - lisab lause
""")
    elif message.content.startswith("$removebot"):
        restr_channels = open(rest_chan, 'a+')
        restr_channels.write(str(message.channel.id) + '''
''')
        restr_channels.close()
        rest_channels = open(rest_chan, 'r+')
        restricted_channels = rest_channels.read().splitlines()
        await message.channel.send('kanal on removeitud')
        print(restricted_channels)
    else:
        rest_channels = open(rest_chan, 'r+')
        restricted_channels = rest_channels.read().splitlines()
        if str(message.channel.id) in restricted_channels:
            return  # Exit the function without sending a message

        # If the message is not in a restricted channel, continue with normal behavior
        filee = open(laused, 'r')
        lause = filee.read().splitlines()
        await message.channel.send(random.choice(lause))
        filee.close()
        rest_channels.close()
        

client.run(TOKEN)