import discord
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

@client.event
async def on_ready():
  print('Logged in as {0.user} homie!'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$ola'):
    await message.channel.send('Boa pá nois meu guerreiro!')


my_secret = os.environ['TOKEN']
client.run(my_secret)
