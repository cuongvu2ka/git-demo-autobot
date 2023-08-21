  #acc chính : nuse 54 68 75
  #NzQ3MDgxMzkxMTI4NDQ0OTM5.YW1omg.ilHiQFu9Z_8M3dkLhTcoBaGtD8M
  #acc sv:
  #OTEwMDAyNjEwMDM4MjU5NzMz.YeEwPg.KVVcM_8jVP7gJtQ6fVDkT-X09nA

import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from numpy import random
from time import sleep
from random import randint
 
#-----SETUP-----#
 
prefix = "?"     
 
#use the .env feature to hide your token
# NzYzNjM2OTEyNDY0MzMwNzYy.G27O0B.1UGdURQrTCcWddk26h-_KmMq1nEPqyX_fhG4Z0
token = "OTI2NDY0NjE0NDA4MDE1OTAz.GO-K_F.GgFhWvzSrPsAPfyfORA300A2ptCIaFrNupogjo"
#---------------#
 
bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.event
async def on_ready():
    print('''WELCOME TO THE OWO AUTO BOT ACCOUNT''')
 
 
@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    
    print("auto OwO  is now **enabled**!")
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(5)
            await asyncio.sleep(13)
 
 
@bot.command()
async def stop(ctx):
    await ctx.message.delete()
    print("auto OwO  is now disabled!")
    global dmcs
    dmcs = False
 

@bot.command(pass_context=True)
async def start(ctx):
    await ctx.message.delete()
    print("auto OwO  is now enabled!")
    count = 0
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            print("The count is:", count, "")
            if count%14 == 0 or count == 0:
              await ctx.send('owopray 797128221929373696')
              print("succefully owopray")
              await asyncio.sleep(1) 
              isCaptcha = await isOwOCaptcha(ctx);
              if isCaptcha == 1:
                dmcs = False
                return
            count = count + 1

            #ob
            await ctx.send('owob')
            print("succefully owob")
            await asyncio.sleep(1)
            isCaptcha = await isOwOCaptcha(ctx);
            if isCaptcha == 1:
              dmcs = False
              return

            #owo
            await ctx.send('owo')
            print("succefully owo")
            await asyncio.sleep(1)
            isCaptcha = await isOwOCaptcha(ctx);
            if isCaptcha == 1:
              dmcs = False
              return

            #oh
            await asyncio.sleep(1)
            await ctx.send('owoh ')
            print("succefully owoh")
            await asyncio.sleep(1)
            isCaptcha = await isOwOCaptcha(ctx);
            if isCaptcha == 1:
              dmcs = False
              return

            #sleep
            sleeptime = random.uniform(10, 15)
            print("sleeping for:", sleeptime, "seconds")
            await asyncio.sleep(sleeptime)
            isCaptcha = await isOwOCaptcha(ctx);
            if isCaptcha == 1:
              dmcs = False
              return
                

async def isOwOCaptcha(ctx):
    authorName = ctx.author.name
    channel = bot.get_channel(ctx.channel.id)
    message = await channel.history(limit=10).flatten()
    for msg in message:
      print(msg.content)
      if 'captcha' in msg.content and msg.author.id == 408785106942164992:
        await ctx.send('?stop')
        await ctx.send('?stop')
        await asyncio.sleep(0.1)
        await ctx.send('oni')
        return 1
      else:
        return 0

bot.run(token, bot=False)
 
