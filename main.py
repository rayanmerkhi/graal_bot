import discord

from discord import app_commands
from discord.ext import commands

from random import randint
from tokened import token_value

from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.command()
@commands.is_owner()
async def synchronize(context):
    response = "Commandes synchronisées avec succès (normalement)"
    try:
        await bot.tree.sync()
    except Exception as e:
        response = "Erreur lors de la synchronisation des commandes dzl:\n" + str(e)

    await context.send(response)

@bot.tree.command(name='roll', description='Permet de jeter les dés')
async def roll(interaction: discord.Interaction, jet: str):
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


class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
        self.to_roll=[]
    
    @discord.ui.button(label="d4",style=discord.ButtonStyle.gray,row=0) # or .primary
    async def dfour(self,interaction:discord.Interaction,button:discord.ui.Button):
        button.disabled=True
        self.to_roll.append(4)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="d6",style=discord.ButtonStyle.gray,row=0) # or .secondary/.grey
    async def dsix(self,interaction:discord.Interaction,button:discord.ui.Button):
        button.disabled=True
        self.to_roll.append(6)
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="d8",style=discord.ButtonStyle.gray,row=0) # or .success
    async def deight(self,interaction:discord.Interaction,button:discord.ui.Button):
        button.disabled=True
        self.to_roll.append(8)
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="d10",style=discord.ButtonStyle.gray,row=1) # or .danger
    async def dten(self,interaction:discord.Interaction,button:discord.ui.Button):
        button.disabled=True
        self.to_roll.append(10)
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="d12",style=discord.ButtonStyle.gray,row=1) # or .secondary/.grey
    async def dtwelve(self,interaction:discord.Interaction,button:discord.ui.Button):
        button.disabled=True
        self.to_roll.append(12)
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="d20",style=discord.ButtonStyle.gray,row=1) # or .success
    async def dtwenty(self,interaction:discord.Interaction,button:discord.ui.Button):
        button.disabled=True
        self.to_roll.append(20)
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="submit",style=discord.ButtonStyle.green,row=2) # or .success
    async def submit(self,interaction:discord.Interaction,button:discord.ui.Button):
        button.disabled=True
        tp=''
        for roll in self.to_roll:
            tp += 'Jet de '
            tp +='d'+str(roll)+': '
            tp+=str(randint(1,roll))+' '
            tp+='\n'
        await interaction.response.send_message(tp)
        self.stop()

@bot.tree.command(name="upgraded",description="Jet de dé avec bouttons")
async def upgraded(interaction: discord.Interaction):
    view=Buttons()
    await interaction.response.send_message("Choisissez les dés",view=view)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

load_dotenv()
bot.run(token_value)