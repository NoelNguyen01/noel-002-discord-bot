import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cai_dat_may_bots')
    @commands.has_permissions(administrator=True)
    async def cai_dat_may_bots(self, ctx):
        await ctx.send('Cài đặt máy bot thành công!')

    @commands.command(name='thong_tin_server')
    @commands.has_permissions(administrator=True)
    async def thong_tin_server(self, ctx):
        server_name = ctx.guild.name
        server_id = ctx.guild.id
        await ctx.send(f'Tên server: {server_name}\nID server: {server_id}')

    @commands.command(name='kiem_tra_bot')
    @commands.has_permissions(administrator=True)
    async def kiem_tra_bot(self, ctx):
        await ctx.send('Bot đang hoạt động bình thường!')

def setup(bot):
    bot.add_cog(Admin(bot))
