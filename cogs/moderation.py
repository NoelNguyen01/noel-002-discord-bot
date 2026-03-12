import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Lệnh để đá một thành viên khỏi máy chủ."""
        await member.kick(reason=reason)
        await ctx.send(f'Dã đuổi {member.mention} khỏi máy chủ. Lý do: {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Lệnh để cấm một thành viên."""
        await member.ban(reason=reason)
        await ctx.send(f'Dã cấm {member.mention} khỏi máy chủ. Lý do: {reason}')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """Lệnh để cấm tiếng nói của một thành viên."""
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(mute_role, reason=reason)
        await ctx.send(f'{member.mention} đã bị cấm tiếng nói. Lý do: {reason}')

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        """Lệnh để cảnh cáo một thành viên."""
        await ctx.send(f'Đã cảnh cáo {member.mention} với lý do: {reason}')


def setup(bot):
    bot.add_cog(Moderation(bot))