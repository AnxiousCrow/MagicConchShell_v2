import os
import discord
from discord.ext import commands
import random
import time
import json
import asyncio
from MagicConchShell import dir_path, load_list

thumbsup = '\U0001f44d'

class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client
    

    # @commands.command()
    # @commands.is_owner()
    # async def test(self, ctx):
    #     await ctx.message.add_reaction(thumbsup)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        if extension != 'Owner':
            self.client.load_extension(f'cogs.{extension}')
            await ctx.message.add_reaction(thumbsup)

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        if extension != 'Owner':
            self.client.unload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction(thumbsup)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        if extension != 'Owner':
            self.client.unload_extension(f'cogs.{extension}')
            time.sleep(.5)
            self.client.load_extension(f'cogs.{extension}')
            await ctx.message.add_reaction(thumbsup)

    @commands.command()
    @commands.is_owner()
    async def servers(self, ctx):
        active_servers = self.client.guilds
        guild_names = []
        num_of_users = 0

        for guild in active_servers:
            guild_names.append(guild.name)
            num_of_users += guild.member_count

        # for name in guile_names:

        await ctx.send(f'{guild_names}, {num_of_users}')

    @commands.command(help='Lists LogGames.txt')
    @commands.is_owner()
    async def log(self, ctx):
        lst = load_list('LogGames.txt')
        str = ''
        for l in lst:
            str += l + '\n'
        await ctx.send(f'```\n{str}\n```')

    @commands.command()
    @commands.is_owner()
    async def addgame(self, ctx, *arg):
        # If no game is entered. Empty tuple
        if not arg:
            time.sleep(.5)
            async with ctx.typing():
                await asyncio.sleep(random.uniform(.5, 2))
            await ctx.send(f"You didn't specify a game...")

        else:
            gamename = ''
            for i in arg:
                gamename += i + " "

            with open(os.path.join(dir_path, 'lists/Statuses.txt'), 'a') as f:
                # Newline has to be at the start so that the gamename isn't an empty string
                f.write("\n" + gamename)

        await ctx.message.add_reaction(thumbsup)

    @commands.command()
    @commands.is_owner()
    async def rebread(self, ctx, channel: discord.TextChannel=None):
        bread = '\U0001f35e'
        bread_dict = {}

        # Delete contents of file
        open(os.path.join(dir_path, 'breads.json'), 'w').close()

        # Gets all breads in a channel that the bot has gifted
        # Need to get the authors of the message and count += 1
        text_channels = []
        #for guild in self.client.guilds:
            #for channel in guild.text_channels:
        for channel in ctx.guild.text_channels:
            text_channels.append(channel)
        #print('**********after guild')
	
        # history = await channel.history(limit=None).flatten()
        print(text_channels)
        for channel in text_channels:
            print(channel)
            #try:
                #history = await channel.history(limit=None)
            #except:
                #return
            # history.reverse()
            async for msg in channel.history(limit=None):
                for reaction in msg.reactions:
                    if reaction.me and str(reaction) == bread:

                        # If user hasn't been added to dict yet
                        author = str(msg.author)
                        if author not in bread_dict:
                            bread_dict[author] = 1
                        else:
                            bread_dict[author] += 1
        print('**********after channel')
        with open(os.path.join(dir_path, 'breads.json'), 'w') as f:
            json.dump(bread_dict, f)

        thumbsup = '\U0001f44d'
        await ctx.message.add_reaction(thumbsup)


def setup(client):
    client.add_cog(Owner(client))
