import os
import discord
from discord.ext import commands
import ffmpeg.audio
from MagicConchShell import dir_path
import time
import asyncio
import random

class Audio(commands.Cog):

    def __init__(self, client):
        self.client = client

    #############################
    # sprite cranberry command
    #############################
    @commands.command(help='$sprite', aliases=['Sprite', 's'])
    async def sprite(self, ctx):

        mp3_path = os.path.join(dir_path, 'audio/SpriteCranberry.mp3')

        channel = ctx.author.voice.channel
        time.sleep(.5)

        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @sprite.error
    async def sprite_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        # if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # wow command
    #############################
    @commands.command(help='$wow (Oh my God, WOW!)', aliases=['Wow', 'WOW'])
    async def wow(self, ctx):

        mp3_path = os.path.join(dir_path, 'audio/wow.mp3')

        channel = ctx.author.voice.channel
        time.sleep(.5)

        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @wow.error
    async def wow_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        # if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # RL command
    #############################
    @commands.command(help='$rl', aliases=['RL'])
    async def rl(self, ctx):

        mp3_path = os.path.join(dir_path, 'audio/ThisIsRocketLeague.mp3')

        channel = ctx.author.voice.channel
        time.sleep(.5)

        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @rl.error
    async def rl_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        # if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # Nice command
    #############################
    @commands.command(help='$nice', aliases=['Nice','NICE'])
    async def nice(self, ctx):

        mp3_path = os.path.join(dir_path, 'audio/click_nice.mp3')

        channel = ctx.author.voice.channel
        time.sleep(.5)

        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @nice.error
    async def nice_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        # if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # Finland command
    #############################
    @commands.command(help='$finland', aliases=['Finland','FINLAND'])
    async def finland(self, ctx):

        mp3_path = os.path.join(dir_path, 'audio/Finland.mp3')

        channel = ctx.author.voice.channel
        time.sleep(.5)

        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @finland.error
    async def finland_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        # if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # Hello There command
    #############################
    @commands.command(help='$hello', aliases=['hellothere','Hello'])
    async def hello(self, ctx):

        mp3_path = os.path.join(dir_path, 'audio/HelloThere.mp3')

        channel = ctx.author.voice.channel
        time.sleep(.5)

        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @hello.error
    async def hello_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        # if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # Wii Sports command
    #############################
    @commands.command(help='$wii', aliases=['Wii', 'WII'])
    async def wii(self, ctx):

        channel = ctx.author.voice.channel
        time.sleep(.5)
        vc = await channel.connect()

        # Get random Wii mp3
        wii_audio = os.path.join(dir_path, 'audio/Wii/')
        rand_mp3 = random.choice(os.listdir(wii_audio))
        mp3_path = os.path.join(wii_audio, rand_mp3)

        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @wii.error
    async def wii_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # KEKW command
    #############################
    @commands.command(help='$kekw (El Risitas)', aliases=['KEKW', 'risitas'])
    async def kekw(self, ctx):

        channel = ctx.author.voice.channel
        time.sleep(.5)
        vc = await channel.connect()

        # Get random laugh mp3
        risitas_audio = os.path.join(dir_path, 'audio/El_Risitas/')
        rand_mp3 = random.choice(os.listdir(risitas_audio))
        mp3_path = os.path.join(risitas_audio, rand_mp3)

        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @kekw.error
    async def kekw_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # Navi command
    #############################
    @commands.command(help='$navi', aliases=['Navi', 'NAVI'])
    async def navi(self, ctx):

        channel = ctx.author.voice.channel
        time.sleep(.5)
        vc = await channel.connect()

        # Get random Wii mp3
        wii_audio = os.path.join(dir_path, 'audio/Navi/')
        rand_mp3 = random.choice(os.listdir(wii_audio))
        mp3_path = os.path.join(wii_audio, rand_mp3)

        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @navi.error
    async def navi_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


    #############################
    # garbage command
    #############################
    @commands.command(help='$garbage', aliases=['GARBAGE', 'garb', 'g'])
    async def garbage(self, ctx):

        mp3_path = os.path.join(dir_path, 'audio/garbage.mp3')

        channel = ctx.author.voice.channel
        time.sleep(.5)

        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(mp3_path))

        while vc.is_playing():
            await asyncio.sleep(.5)

        await vc.disconnect()


    # on_error
    @garbage.error
    async def garbage_handler(self, ctx, error):
        time.sleep(.5)
        async with ctx.typing():
            await asyncio.sleep(random.uniform(.5, 1))
        await ctx.send(file=discord.File(os.path.join(dir_path, 'gifs/NoPower.gif')))
        await ctx.send("You are not in a voice channel...")


def setup(client):
    client.add_cog(Audio(client))

