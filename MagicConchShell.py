import os
import discord
from discord.ext import commands, tasks
import json
import random
import time

# import nacl
# import ffmpeg.audio
# import asyncio
# from time import gmtime, strftime

start_time = time.time()
client = commands.Bot(command_prefix='$')

# Gets the current directory
#dir_path = os.path.dirname(os.path.realpath('__file__'))
dir_path = '/home/ubuntu/Discord/MagicConchShell/'
token_path = os.path.join(dir_path, 'token.txt')
token = open(token_path, 'r').read()


# Loads response lists
def load_list(file_name):
    list_path = os.path.join(dir_path, file_name)
    with open(list_path) as f:
        lst = f.read().splitlines()
    return lst


status_list = load_list('lists/Statuses.txt')


#############################
# Start-up command
#############################
@client.event
async def on_ready():
    print(f'{client.user} bot ready!')
    await client.change_presence(activity=discord.Game(name=random.choice(status_list)))
    change_status.start()


##########################################################
# Looping command
# Changes the bot's game status every x minutes
##########################################################
@tasks.loop(minutes=120)
async def change_status():
    await client.change_presence(activity=discord.Game(name=random.choice(status_list)))


#############################
# Message specifics
#############################
@client.event
async def on_message(message):
    try:
        # Adds Bread reaction to random message
        if random.randint(0, 99) == 0:
        # if message.content.lower() == 'bread':
            bread = '\U0001f35e'
            await message.add_reaction(bread)

            # Open breads.json and += 1 for author
            with open(os.path.join(dir_path, 'breads.json'), 'r') as f:
                bread_dict = json.load(f)
            # print(type(bread_dict), bread_dict)

            # Checks to see if the author is already in 'breads.json'
            author = str(message.author)
            if author not in bread_dict:
                bread_dict[author] = 1
            else:
                bread_dict[author] += 1

            # Updates the file
            with open(os.path.join(dir_path, 'breads.json'), 'w') as f:
                json.dump(bread_dict, f)


        matches = ['mcs', 'shell', 'conch', 'bot']
        if any(x in message.content.lower() for x in matches):
            time.sleep(1)
            if random.randint(0, 99) < 5:
                await message.add_reaction(discord.utils.get(message.guild.emojis, name='MCS'))

        matches = ['haha', 'lol']
        if any(x in message.content.lower() for x in matches):
            time.sleep(1)
            if random.randint(0, 99) < 5:
                await message.add_reaction(discord.utils.get(message.guild.emojis, name='lol'))

        matches = ['psyonix']
        if any(x in message.content.lower() for x in matches):
            time.sleep(1)
            if random.randint(0, 99) < 75:
                await message.add_reaction(discord.utils.get(message.guild.emojis, name='WWWAAAA'))

        matches = ['ok', 'sounds good', 'nice!', 'cool!', 'hop on', 'back on']
        if any(x in message.content.lower() for x in matches):
            time.sleep(1)
            if random.randint(0, 99) < 5:
                await message.add_reaction(discord.utils.get(message.guild.emojis, name='hooookay'))

        matches = [':(', '):', 'noo', 'sorry', "i don't think so",
                   ' f ', 'rip', 'sad', "can't", "won't", 'maybe later', 'maybe someday']
        if any(x in message.content.lower() for x in matches):
            time.sleep(1)
            if random.randint(0, 99) < 5:
                await message.add_reaction(discord.utils.get(message.guild.emojis, name='sads'))

        matches = ['upload']
        if any(x in message.content.lower() for x in matches):
            time.sleep(1)
            if random.randint(0, 99) < 50:
                await message.add_reaction(discord.utils.get(message.guild.emojis, name='bruhwack'))

    except:
        pass

    # This line allows on_message and commands
    await client.process_commands(message)


# Load Cogs
for filename in os.listdir(os.path.join(dir_path, 'cogs/')):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(token)
