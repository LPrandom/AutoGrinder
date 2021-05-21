import discord
import time
import random
import ctypes

from discord.ext import commands
from config import token, prefix, loops_control

bot = commands.Bot(prefix, self_bot=True)
loops = (int(loops_control))
bot.togglegrind = False

ctypes.windll.kernel32.SetConsoleTitleW(f'AuTo GrInDeR ;) | Counter = 0/{loops}')

def words():
	wordlist = ['men', 'feet', 'women', 'poo']
	word = random.choice(wordlist)
	return word

@bot.event
async def on_ready():
	print(f'Ready | {bot.user}')

@bot.command()
async def toggle(ctx):
	await ctx.message.delete()
	if bot.togglegrind == False:
		print(f'Toggled on! | Do {prefix}autogrind to grind!')
		bot.togglegrind = True

	elif bot.togglegrind == True:
		print(f'Toggled off! | Do {prefix}toggle to turn it on!')
		bot.togglegrind = False

	else:
		print('Something went wrong... | Resetting it back to defualt!')
		bot.togglegrind = False

@bot.command()
async def autogrind(ctx):
	await ctx.message.delete()
	counter = 0
	if bot.togglegrind == True:
		for _i in range(loops):
			try:
				own = counter + 1
				counter = own
				ctypes.windll.kernel32.SetConsoleTitleW(f'AuTo GrInDeR ;) | Counter = {counter}/{loops}')
				msg = await ctx.send(f'I like {words()}')
				await msg.delete()
				if bot.togglegrind == False:
					return

				time.sleep(61.5)

			except Exception as e:
				print('Something went wrong! Stopping the grinder!')
				return

	elif bot.togglegrind == False:
		await ctx.send(f'Toggle the grinder doing "{prefix}toggle"')

	else:
		print('Something went wrong!')

bot.run(token, bot=False)