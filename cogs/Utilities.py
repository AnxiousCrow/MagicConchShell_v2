import os
import discord
from discord.ext import commands
import json
import time
from time import gmtime, strftime
import asyncio
import random
from collections import OrderedDict
from MagicConchShell import start_time, dir_path


# For $game command
def log_game(gamename, user):
    log_path = os.path.join(dir_path, 'LogGames.txt')
    with open(log_path, 'a') as log_file:
        log_file.write(gamename + " " + user + '\n')


# For $uptime command
def get_uptime():
    end_time = time.time()
    return(strftime("%H:%M:%S", gmtime(int('{:.0f}'.format(float(str((end_time-start_time))))))))


class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client
    

    #############################
    # ping command
    #############################
    @commands.command(help="$ping", aliases=['p'])
    async def ping(self, ctx):
        await ctx.send(f'Bot latency: {round(self.client.latency * 1000)}ms')


    #############################
    # uptime command
    #############################
    @commands.command(help="$uptime", aliases=['u'])
    async def uptime(self, ctx):
        await ctx.send(f'Uptime: {get_uptime()}')

    
    #############################
    # game command
    #############################
    @commands.command(help="$game [Name of Game]")
    async def game(self, ctx, *arg):
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
            
            time.sleep(.5)
            async with ctx.typing():
                await asyncio.sleep(random.uniform(.5, 2))

            await ctx.send(f'Now playing {gamename}')
            await self.client.change_presence(activity=discord.Game(name=gamename))
            log_game(gamename, str(ctx.author))


    #############################
    # dice command
    #############################
    @commands.command(help='$dice 3d18 (Rolls 3 dice with 18 sides)')
    async def dice(self, ctx, *, arg):

        arg = arg.lower()

        if 'd' in arg:
            dice_params_lst = arg.split('d')
            num_of_dice = int(dice_params_lst[0])
            num_of_sides = int(dice_params_lst[1])

            if num_of_dice <= 0 or num_of_sides <= 0:
                async with ctx.typing():
                    await asyncio.sleep(random.uniform(.5, 2))
                await ctx.send(f'```{arg}``` is not valid. You must use positive intergers.')
                return

            roll_lst = []
            for _ in range(num_of_dice):
                roll_lst.append(random.randint(1, num_of_sides))

            embed = discord.Embed(
                description=f":game_die: {arg} {roll_lst}", color=0xff0000)
            await ctx.send(embed=embed)
        else:
            async with ctx.typing():
                await asyncio.sleep(random.uniform(.5, 2))
            await ctx.send(f'"{arg}" is not valid syntax.')
            await ctx.send('To roll 3 dice with 18 sides:\n```$dice 3d18```')


    # on_error
    @dice.error
    async def dice_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        await ctx.send("Invalid syntax.")
        await ctx.send('To roll 3 dice with 18 sides:\n```$dice 3d18```')


    #############################
    # die command
    #############################
    @commands.command(help='$die (This automatically rolls a 1d6)')
    async def die(self, ctx):
        roll = random.randint(1, 6)
        embed = discord.Embed(
            description=f":game_die: 1d6 [{roll}]", color=0xff0000)
        await ctx.send(embed=embed)
        # await ctx.send(f'```1d6 [{roll}]```')


    #############################
    # Bread count command
    #############################
    @commands.command(help='$bread (Lists bread stats)')
    async def bread(self, ctx):
        bread = '\U0001f35e'
        
        # Get bread data
        with open(os.path.join(dir_path, 'breads.json'), 'r') as f:
            bread_dict = json.load(f)

        # Create embed
        embed = discord.Embed(
            title='Bread Stats!',
            url='https://discord.com/assets/b4145d2678321d6d3376f1c88604fd42.svg',
            icon_url='https://images.emojiterra.com/twitter/v13.0/512px/1f35e.png',
            description=f'Shows number of times users have been blessed with {bread} by The MagicConchShell.\n------------------------',
            color=0xff0000
        )
        embed.set_thumbnail(url='https://images.emojiterra.com/twitter/v13.0/512px/1f35e.png')
        # embed.set_author(name="MagicConchShell", url='https://github.com/AnxiousCrow/MagicConchShell', icon_url='https://cdn.discordapp.com/avatars/754734227651690526/3da3291519ea3abc53cb2409e8686c67.png?size=256')


        bread_dict_sorted = dict(sorted(bread_dict.items(), key=lambda item: item[1], reverse=True))
        for username, num in bread_dict_sorted.items():
            # username = username[:-5]
            # if num == 1:
            embed.add_field(name=f'{username}', value=f'{num} {bread}', inline=True)
            # else:
                # embed.add_field(name=f'{username}', value=f'{num} {bread}', inline=True)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utilities(client))
