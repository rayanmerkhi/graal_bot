import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)

@tree.command(name='sync', description='Owner only')
async def sync(interaction: discord.Interaction):
    if interaction.user.id == :
        await tree.sync()
        print('Command tree synced.')
    else:
        await interaction.response.send_message('U are not the owner')

@tree.command(name='roll', description='Permet de jeter les dés')
async def roll(interaction: discord.Interaction)