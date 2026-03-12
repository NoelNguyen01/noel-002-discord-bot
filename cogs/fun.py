import discord
from discord.ext import commands
import random
import requests

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='joke')
    async def joke(self, ctx):
        response = requests.get('https://official-joke-api.appspot.com/jokes/random')
        joke = response.json()
        await ctx.send(f"{joke['setup']}\n{joke['punchline']}")

    @commands.command(name='avatar')
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send(member.avatar_url)

    @commands.command(name='coinflip')
    async def coinflip(self, ctx):
        result = random.choice(['Đầu', ' Xác'])
        await ctx.send(f"Kết quả: {result}")

    @commands.command(name='dice')
    async def dice(self, ctx, sides: int = 6):
        if sides < 1:
            await ctx.send('Số mặt phải lớn hơn 0!')
            return
        result = random.randint(1, sides)
        await ctx.send(f"Kết quả: {result}")


def setup(bot):
    bot.add_cog(Fun(bot))
