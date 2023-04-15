import requests
import random
import secrets
import discord
from discord.ext import commands
import asyncio
import ast
import json



intents = discord.Intents.all()

bot = commands.Bot(command_prefix="$", intents=intents, activity = discord.Game(name = 'your great-grandfather'))

opentoken = open("token.txt", 'r')
TOKEN = opentoken.read()

laused = 'laused.txt'

kaheksaball = "8ball.txt"

noolfail = 'nool.txt'

rest_chan = 'rest_chan.txt'

async def get_message_history(user_id, channel):
    user = await bot.fetch_user(user_id)
    async for message in channel.history(limit=200):
        if message.author == user or message.author == bot.user:
            await channel.send(f'{message.created_at}: {message.author}: {message.content}')
            
@bot.command(help='shutdownib boti')
@commands.is_owner()
async def shutdown(ctx):
    exit()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    rest_channels = open(rest_chan, 'r+')
    restricted_channels = rest_channels.read().splitlines()
    print(restricted_channels)
    rest_channels.close()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    

    if "ekre" in message.content:
        ekre_open = open('EKRE.txt', 'r')
        ekre_read = ekre_open.read()
        await message.channel.send(ekre_read)
        ekre_open.close()
        return
    if "EKRE" in message.content:
        ekre_open = open('EKRE.txt', 'r')
        ekre_read = ekre_open.read()
        await message.channel.send(ekre_read)
        ekre_open.close()
        return
    if "lappa kotte" in message.content:
        await message.channel.send("ma ei lappa kotte")
        return
    if not message.content.startswith(bot.command_prefix): # check if the message is not a command
        rest_channels = open(rest_chan, 'r+')
        restricted_channels = rest_channels.read().splitlines()
        if str(message.channel.id) in restricted_channels:
            return  # Exit the function without sending a ctx

        # If the ctx is not in a restricted channel, continue with normal behavior
        with open("laused.txt") as f:
            data = json.load(f)

        random_lause = random.choice([d["lause"] for d in data])

        await message.channel.send(random_lause)

        rest_channels.close()
    else:
        try:
            await bot.process_commands(message)
        except Exception as e:
            await message.channel.send("""vale command tumba.
Error: {e}""")
    

@bot.command(help='teeb matemaatikat')
async def math(ctx, ekvatsioon: str):
    await ctx.channel.send('mathing:nerd:')
    await asyncio.sleep(1)
    mesg_con = ctx.message.content.replace('$math ', '')
    if mesg_con == "me+yourmom":
        tehe = "yourdad"
    elif mesg_con == "me+your mom":
        tehe = "your dad"
    else:
        try:
            tehee = ast.parse(ekvatsioon, mode='eval')
        except SyntaxError:
            return    # not a Python expression
        if not all(isinstance(node, (ast.Expression,
                ast.UnaryOp, ast.unaryop,
                ast.BinOp, ast.operator,
                ast.Num)) for node in ast.walk(tehee)):
            return    # not a mathematical expression (numbers and operators)
        tehe = eval(compile(tehee, filename='', mode='eval'))
    tehet = (str(mesg_con) + "=" + str(tehe))
    print(tehet)
    await ctx.channel.send(tehet)
    
    
@bot.command(help='lisab scoori')
async def score(ctx, mesag_con: int):
    file = 'scoor.txt'
    openscoor = open(file,"r+")
    scoor = openscoor.read()
    openscoor.close()
    openscore = open(file,"w+")
    openscore.write(str(int(scoor) + mesag_con))
    openscore.close()
    opnscr = open(file,"r+")
    scoree = opnscr.read()
    await ctx.channel.send(scoree)
    opnscr.close()
    
    
@bot.command(help=':skull:')
async def meth(ctx):
    await ctx.channel.send('mething :100:')
    await asyncio.sleep(1)
    await ctx.channel.send(':100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100: :100:')
    
    
@bot.command(help='genereerib nitrot')
async def nitrogen(ctx, nitro: int):
    await ctx.channel.send("*generating free nitro*")
    def gen_gift(length):
        return secrets.token_hex(length // 2)

    if nitro <= 200:
        for j in range(nitro):
            for i in range(25):
                GIFT_CODE = ('discord.gift/' + gen_gift(16))
                
                response = requests.get(f'https://discord.com/api/v6/entitlements/gift-codes/{GIFT_CODE}', headers={'Authorization': f'Bot {TOKEN}'})
                # Check the status code of the response
                if response.status_code == 200:
                    # If the status code is 200, the gift code is valid
                    await ctx.channel.send('Gift code is valid:   ' + 'discord.gift/' + '{GIFT_CODE}')
                    break
            await ctx.channel.send("didn't find nitro")
            await asyncio.sleep(1)
    else:
        await ctx.channel.send("ei tee nii palju nitrot")
            
@bot.command(help='lisab suvalistesse lausetesse lause, mis sina kirjutasid')     
async def addlause(ctx, *, lause):
#     fail = open(laused, 'a')
#     
#     fail.write("""
# """+ lause)
#     
#     fail.close()

    # Load existing lauses from the JSON file
    with open('laused.txt', 'r') as f:
        lauses = json.load(f)

    # Add the new lause to the list
    lauses.append({"lause": lause})

    # Save the updated list of lauses to the JSON file
    with open('laused.txt', 'w') as f:
        json.dump(lauses, f)
    await ctx.channel.send('lause "' + lause + '" on salvestatud')
    
@bot.command(help='kaheksapall annab vastuseid')
async def kaheksapall(ctx, kusimus: str):
    fileee = open(kaheksaball, 'r')
    lausee = fileee.read().splitlines()
    await ctx.channel.send(("Minu vastus sinu kusimusele '" + kusimus + "' on: " + random.choice(lausee)))
    fileee.close()
    
    
@bot.command(help='teeb posu nooli')
async def nool(ctx, noolarv: int):
    fliec = open(noolfail, 'w')
    fliec.close()
    for l in range(noolarv):
        noollength = random.randint(1, 101)
        fileeee = open(noolfail, 'a+')
        for k in range(noollength):
            fileeee.write('-')
        fileeee.write(">")
        fileeee.close()
        fileeeee = open(noolfail, 'r')
        await ctx.channel.send(fileeeee.read())
        print(fileeeee.read())
        fileeee.close()
        filew = open(noolfail, 'w')
        filew.close()
        
        
@bot.command(help='kasutu')
async def commandid(ctx):
    await ctx.channel.send("""Boti prefiks on $
Commandid:
nool - teeb kindla koguse nooli
nitrogen - proovib genereerida nitrot
math - lahendab tehte
meth - :skull:
8pall - see annab vastuse
score - lisab antud koguse skoori uleuldisesse skoori kogusesse
addlause - lisab lause
invite - 
""")
        
        
@bot.command(help='ei lase botil saata suvalisi lauseid selles kanalis')
async def shutup(ctx):
    restr_channels = open(rest_chan, 'a+')
    restr_channels.write(str(ctx.channel.id) + '''
''')
    restr_channels.close()
    rest_channels = open(rest_chan, 'r+')
    restricted_channels = rest_channels.read().splitlines()
    await ctx.channel.send('kanal on removeitud')
    print(restricted_channels)
    
    
# @bot.command()
# async def history(ctx, user_id: str):
#     channel = ctx.channel
#     await get_message_history(user_id, channel)
    
@bot.command(help='teeb invite lingi botile')
async def invite(ctx):
    await ctx.channel.send("""Siin on invite:
https://discord.com/api/oauth2/authorize?client_id=1058116264628850768&permissions=8&scope=bot""")
        
        
    
bot.run(TOKEN)