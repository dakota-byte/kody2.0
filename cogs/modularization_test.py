# The vital discord imports
import discord
from discord.ext import commands

# Misc. imports


class modularization_test(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(aliases=['modularization_test'], brief="Boilerplate for adding modules", description="N/A")
    async def kodys_module_test(self, ctx):
        await ctx.send('📦📦📦')

# client is bot. adds this module to Kody
async def setup(client):
    await client.add_cog(modularization_test(client))