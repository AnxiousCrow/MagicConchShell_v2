import os
import discord
from discord.ext import commands
import time
import asyncio
import random
from MagicConchShell import dir_path, load_list


ConchShellResponses = load_list('lists/ConchShellResponses.txt')
sus_list = load_list('lists/Sus.txt')
food_list = load_list('lists/Food.txt')


class General(commands.Cog):

    def __init__(self, client):
        self.client = client


    #############################
    # percent command
    #############################
    @commands.command(help="$percent [what percentage is x?]", aliases=['whatpercent'])
    async def percent(self, ctx, *arg):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        await ctx.send(f'{random.randint(0, 100)}%')


    #############################
    # mcs command
    #############################
    @commands.command(help="$mcs [Yes or No question]", aliases=['conch', 'shell'])
    async def mcs(self, ctx, *, question):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        await ctx.send(random.choice(ConchShellResponses))

    # on_error
    @mcs.error
    async def mcs_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        # time.sleep(1)
        await ctx.send(f"You didn't ask me anything...")
        
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        await ctx.send(f"Try asking something like this:\n```$mcs am I stupid?```")

    
    #############################
    # sus command
    #############################
    @commands.command(help='$sus [the sus]', aliases=['sus?', 'howsus', 'howsus?'])
    async def sus(self, ctx, *, arg):

        time.sleep(.5)
        matches = ['mcs', 'yourself', 'magic', 'conch', 'shell', 'i']
        # $sus mcs
        if any(x in arg.lower() for x in matches) or str(arg) == '<@!754734227651690526>':
            async with ctx.typing():
                await asyncio.sleep(random.uniform(.5, 2))
            await ctx.send(f'How dare you even ask...')
            return

        else:
            async with ctx.typing():
                await asyncio.sleep(random.uniform(.5, 2))
            await ctx.send(random.choice(sus_list))

    # on_error
    @sus.error
    async def sus_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        await ctx.send(random.choice(sus_list))


    #############################
    # price command
    #############################
    @commands.command(help="$price [how much is x worth?]")
    async def price(self, ctx, *, arg):
        time.sleep(.5)

        matches = ['mcs', 'yourself', 'magic', 'conch', 'shell']
        if any(x in arg.lower() for x in matches) or str(arg) == '<@!754734227651690526>':
            async with ctx.typing():
                await asyncio.sleep(random.uniform(.5, 2))
            await ctx.send(f"Priceless")
        else:
            async with ctx.typing():
                await asyncio.sleep(random.uniform(.5, 2))
            await ctx.send(f'${random.randint(0, 60)}.{"%02d" % random.randint(0, 99)}')


    # on_error
    @price.error
    async def price_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        await ctx.send(f"You didn't say what you wanted appraised...")


    #############################
    # slap command
    #############################
    @commands.command(help="$slap [name]")
    async def slap(self, ctx, *, arg):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))

        matches = ['mcs', 'yourself', 'magic', 'conch', 'shell', 'i']
        matches2 = ['me', 'myself']

        # $slap mcs
        if any(x in arg.lower() for x in matches) or str(arg) == '<@!754734227651690526>':
            await ctx.send(f':raised_hand: *Slap!* {ctx.author.mention} has been punished for trying to be smart.')
            return

        # $slap me
        if any(x in arg.lower() for x in matches2):
            await ctx.send(f':raised_hand: *Slap!* {ctx.author.mention} has been punished.')
            return

        else:
            await ctx.send(f':raised_hand: *Slap!* {arg} has been punished.')

    # on_error
    @slap.error
    async def slap_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        await ctx.send(f"You didn't say who to slap...")

        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))
        await ctx.send(f':raised_hand: *Slap!* {ctx.author.mention} has been punished for not saying who to slap.')





    #############################
    # feed command
    #############################
    @commands.command(help='$feed [@person]')
    async def feed(self, ctx, person):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))

        food = random.choice(food_list)

        matches = ['mcs', 'shell', 'conch', 'bot', 'yourself', 'magic']
        matches2 = ['me', 'myself']

        # If they say $feed mcs
        if any(x in str(person).lower() for x in matches) or str(person) == '<@!754734227651690526>':
            await ctx.send(f"I'm a ~~bot~~ **Magic Conch**. I don't require the {food} like meer mortals.")
            return

        # If they say $feed me or $feed myself
        if any(x in str(person).lower() for x in matches2):
            embed = discord.Embed(
                description=f"Forces {food} down {ctx.author.display_name}'s throat", color=0xff0000)
            await ctx.send(embed=embed)
            return

        else:
            embed = discord.Embed(
                description=f"Forces {food} down {person}'s throat", color=0xff0000)
            await ctx.send(embed=embed)
            return


    # on_error
    @feed.error
    async def feed_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 2))

        # if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You didn't tell me who to feed...")





def setup(client):
    client.add_cog(General(client))