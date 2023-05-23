# The vital discord imports
import asyncio
import discord
from discord.ext import commands

# Misc. imports
import os
import json

# Declaring intents & declaring prefix, and creating bot
prefix = '!'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

with open('config.json') as file:
    config = json.load(file)

bot_token = config['token']

# Load all of our existing cogs
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(bot_token)

# on_ready() event fires when the file is run, signaling Kody's alive
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    # Assign a role to the member
    role = discord.utils.get(member.guild.roles, name="Intern 💾")
    if role is not None:
        await member.add_roles(role)

    # Send a welcome message
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel is not None:
        await channel.send(f"come quick, {member.mention}, we need help.")

asyncio.run(main())