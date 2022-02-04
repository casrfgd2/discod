import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive
import os


#-----SETUP-----#

prefix = ":"

#use the .env feature to hide your token

keep_alive()
token = os.environ.get('TOKEN_BOT')
target = "914724228270530601"

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Flamer", color=420699, description=f"**{prefix}start**\nsends Flame\n\n**{prefix}stop**\nstops autodank.")
  embed.set_thumbnail(url="Nil")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def start(ctx):
	await ctx.message.delete()
	
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(.5)	    					
			await ctx.send('~execute b1 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b1 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b1 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b1 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b2 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b2 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b2 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b2 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b3 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b3 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b3 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b3 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b4 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b4 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b4 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b4 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b5 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b5 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b5 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b5 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b6 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b6 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b6 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b6 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b7 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b7 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b7 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b7 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b8 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b8 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b8 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b8 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b9 drink')
			await asyncio.sleep((.5))
			await ctx.send('~execute b9 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b9 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b9 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b10 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b10 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b10 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b10 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b11 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b11 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b11 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b11 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b12 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b12 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b12 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b12 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b13 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b13 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b13 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b13 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b14 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b14 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b14 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b14 shoot (target)')
			await asyncio.sleep(120)
			await ctx.send('~execute b15 drink')
			await asyncio.sleep(.5)
			await ctx.send('~execute b15 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b15 shoot (target)')
			await asyncio.sleep(20)
			await ctx.send('~execute b15 shoot (target)')
			await asyncio.sleep(120)
			
												
@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('Flamed!')
	global dmcs
	dmcs = False

@bot.command()
async def lma(ctx):
  await ctx.message.delete()
  activity = discord.Game(name="Lullaby", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}
██

 Flame is ready!
''')

bot.run(token, bot=False) 
