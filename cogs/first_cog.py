import discord
from discord.ext import commands


class FirstCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["test"])
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Pong!",
            colour=int("19C7FC", 16),
            description=f"The bot's ping is: `{round(self.client.latency, 2)}`"
        )
        await ctx.send(embed=embed)
