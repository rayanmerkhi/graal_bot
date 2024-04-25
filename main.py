import discord

from discord import app_commands
from discord.ext import commands

from tokened import token_value
from src.bouton_normal import ButtonsNorm
from src.bouton_avantage import ButtonsAv
from src.bouton_full import ButtonsFull
from random import randint
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix="/", intents=intents)
context=discord.ext.commands.Context

@bot.command()
@commands.is_owner()
async def synchronize(context):
    response = "Commandes synchronisées avec succès (normalement)"
    try:
        await bot.tree.sync()
    except Exception as e:
        response = "Erreur lors de la synchronisation des commandes dzl:\n" + str(e)

    await context.send(response)

@bot.tree.command(name='jet_simple', description='Permet de jeter les dés')
async def jet_simple(interaction: discord.Interaction, jet: str):
    x=jet.split(" ")
    tp=''
    for roll in x:
        num = roll.split("d")
        tp += 'Jet de '
        tp +=str(num[0])+'d'+str(num[1])+': '
        for i in range(int(num[0])):
            tp+=str(randint(1,int(num[1])))+' '
        tp+='\n'
    await interaction.response.send_message(tp)


@bot.tree.command(name="roll",description="Jet de dé")
async def roll(interaction: discord.Interaction, nb_dice:str='0', value:str='1000'):
    # ButtonsNorm est une class qui represente le design des boutons
    # de base nb_dice a 0 car comme ca pas de blocage
    view=ButtonsNorm(nb_dice=int(nb_dice),val=int(value))
    await interaction.response.send_message("Choisissez les dés",view=view,ephemeral=True)

@bot.tree.command(name="roll_avantage",description="Jet de dé avec avantage")
async def roll_avantage(interaction: discord.Interaction, nb_dice:str='0', value:str='1000'):
    # ButtonsAv est une class qui represente le design des boutons
    # de base nb_dice a 0 car comme ca pas de blocage
    view=ButtonsAv(nb_dice=int(nb_dice),val=int(value))
    await interaction.response.send_message("Choisissez les dés",view=view,ephemeral=True)

@bot.tree.command(name="roll_full",description="Jet de dé avec full")
async def roll_full(interaction: discord.Interaction, nb_dice:str='0', value:str='1000'):
    # ButtonsFull est une class qui represente le design des boutons
    # de base nb_dice a 0 car comme ca pas de blocage
    view=ButtonsFull(nb_dice=int(nb_dice),val=int(value))
    await interaction.response.send_message("Choisissez les dés",view=view,ephemeral=True)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

load_dotenv()
bot.run(token_value)