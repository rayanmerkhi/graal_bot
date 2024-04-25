import discord

from random import randint

class ButtonsAv(discord.ui.View):
    def __init__(self, *, timeout=180,nb_dice=3,val=30):
        super().__init__(timeout=timeout)
        self.to_roll=[]
        self.rest=nb_dice
        self.val=val
        self.retry=True
    
    @discord.ui.button(label="d4",style=discord.ButtonStyle.gray,row=0) # or .primary
    async def dfour(self,interaction:discord.Interaction,button:discord.ui.Button):
        if 4 in self.to_roll:
           self.retry=False
        if not self.retry:
            button.disabled=True
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                if child.row!=2:
                    child.disabled=True

        self.to_roll.append(4)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="d6",style=discord.ButtonStyle.gray,row=0) # or .secondary/.grey
    async def dsix(self,interaction:discord.Interaction,button:discord.ui.Button):
        if 6 in self.to_roll:
           self.retry=False
        if not self.retry:
            button.disabled=True
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                if child.row!=2:
                    child.disabled=True
        self.to_roll.append(6)
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="d8",style=discord.ButtonStyle.gray,row=0) # or .success
    async def deight(self,interaction:discord.Interaction,button:discord.ui.Button):
        if 8 in self.to_roll:
           self.retry=False
        if not self.retry:
            button.disabled=True
        self.to_roll.append(8)
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                if child.row!=2:
                    child.disabled=True
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="d10",style=discord.ButtonStyle.gray,row=1) # or .danger
    async def dten(self,interaction:discord.Interaction,button:discord.ui.Button):
        if 10 in self.to_roll:
           self.retry=False
        if not self.retry:
            button.disabled=True
        self.to_roll.append(10)
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                if child.row!=2:
                    child.disabled=True
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="d12",style=discord.ButtonStyle.gray,row=1) # or .secondary/.grey
    async def dtwelve(self,interaction:discord.Interaction,button:discord.ui.Button):
        if 12 in self.to_roll:
           self.retry=False
        if not self.retry:
            button.disabled=True
        self.to_roll.append(12)
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                if child.row!=2:
                    child.disabled=True

        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="d20",style=discord.ButtonStyle.gray,row=1) # or .success
    async def dtwenty(self,interaction:discord.Interaction,button:discord.ui.Button):
        if 20 in self.to_roll:
           self.retry=False
        if not self.retry:
            button.disabled=True
        self.to_roll.append(20)
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                if child.row!=2:
                    child.disabled=True
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="submit",style=discord.ButtonStyle.green,row=2) # or .success
    async def submit(self,interaction:discord.Interaction,button:discord.ui.Button):
        tp += ' a lancé :'
        crit = True
        sum=0
        for roll in self.to_roll:
            tp +='d'+str(roll)+': '
            nb=randint(1,roll)
            sum+=nb
            tp+=str(nb)+' '
            tp+='\n'
            if roll != nb:
                crit =False
        tp+='Somme: '+str(sum)+'\n'
        if crit:
            tp+='Succès Critique !\n'
        elif abs(self.val-sum)<15 & self.val!=1000:
            tp+='Echec Critique !\n'
        await interaction.response.send_message(f'{interaction.user.mention}'+tp)
        for child in self.children:
            child.disabled=True
        self.stop()
