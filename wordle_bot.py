# Imports
import os
from discord.ext import commands
from dotenv import load_dotenv


# Connect the bot to Discord service.
print('Connecting to Discord...')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')


# Log that the bot has connected to Discord.
@bot.event
async def on_ready():
  print(f'{bot.user.name} has connected to Discord')


# Command to check scoreboard.
@bot.command(name='sb', help='Displays the scoreboard for Wordle')
async def scoreboard(ctx):
  response = 'SCOREBOARD'
  await ctx.send(response)


# Command to upload Wordle data.
@bot.command(name='word', help='Used to upload Wordle results')
async def upload_wordle(ctx):
  wordle = ctx.message.content.lstrip('!wordle').split()
  wordle_number   = wordle[1]
  wordle_score    = wordle[2]
  wordle_guesses  = wordle[3:]

  response = wordle_guesses
  await ctx.send(response)


bot.run(TOKEN)