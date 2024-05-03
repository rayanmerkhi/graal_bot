import discord

from random import randint

class ButtonsFull(discord.ui.View):
    def __init__(self, *, timeout=180,nb_dice=3,val=30):
        super().__init__(timeout=timeout)
        self.rest=nb_dice
        self.val=val
        self.rolled=[]
        self.result=[]
        self.response_msg=None
        self.tp = None
    
    @discord.ui.button(label="d4",style=discord.ButtonStyle.gray,row=0) # or .primary
    async def dfour(self,interaction:discord.Interaction,button:discord.ui.Button):
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                child.disabled=True
        
        await interaction.response.edit_message(view=self)
        await self.submit(interaction=interaction, tr=4)

    @discord.ui.button(label="d6",style=discord.ButtonStyle.gray,row=0) # or .secondary/.grey
    async def dsix(self,interaction:discord.Interaction,button:discord.ui.Button):
        self.rest-=1
        if self.rest ==0:
            for child in self.children:                
                child.disabled=True

        await interaction.response.edit_message(view=self)
        await self.submit(interaction=interaction, tr=6)
    
    @discord.ui.button(label="d8",style=discord.ButtonStyle.gray,row=0) # or .success
    async def deight(self,interaction:discord.Interaction,button:discord.ui.Button):
        (8)
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                child.disabled=True

        await interaction.response.edit_message(view=self)
        await self.submit(interaction=interaction, tr=8)
    
    @discord.ui.button(label="d10",style=discord.ButtonStyle.gray,row=1) # or .danger
    async def dten(self,interaction:discord.Interaction,button:discord.ui.Button):
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                child.disabled=True

        await interaction.response.edit_message(view=self)
        await self.submit(interaction=interaction, tr=10)
    
    @discord.ui.button(label="d12",style=discord.ButtonStyle.gray,row=1) # or .secondary/.grey
    async def dtwelve(self,interaction:discord.Interaction,button:discord.ui.Button):
        self.rest-=1
        if self.rest ==0:
            for child in self.children:
                child.disabled=True


        await interaction.response.edit_message(view=self)
        await self.submit(interaction=interaction, tr=12)
    
    @discord.ui.button(label="d20",style=discord.ButtonStyle.gray,row=1) # or .success
    async def dtwenty(self,interaction:discord.Interaction,button:discord.ui.Button):
        self.rest-=1
        if self.rest ==0:
            for child in self.children:                
                child.disabled=True

        await interaction.response.edit_message(view=self)
        await self.submit(interaction=interaction, tr=20)
    
    async def submit(self,tr:int,interaction:discord.Interaction):
        tp= ' a lancé :\n'
        crit = True
        explode=[]
        sum=0
        self.result.append(randint(1,tr))
        self.rolled.append(tr)
        
        
        for i in range(len(self.rolled)):
            tp +='d'+str(self.rolled[i])+': '
            sum+=self.result[i]
            tp+=str(self.result[i])+' '
            tp+='\n'
        
        tp+='Somme: '+str(sum)+'\n'
        for i in range(len(self.rolled)):
            if(self.rolled[i]!=self.result[i]):
                crit=False
        if(crit):
            tp+='Succès Critique !\n'
            for i in range(len(self.rolled)):
                tp+=f'{self.rolled[i]==self.result[i] }'

        if(self.val != 1000):
            if(sum>self.val and sum<self.val+10):
                tp+='Succès !\n'
            elif(sum==self.val):
                tp+='Succès Critique !\n'
            elif(sum<self.val and sum>self.val-10):
                tp+='Echec !'
            else:
                tp+='Echec Critique !\n'

        vu=discord.ui.View()
        for i in range(len(explode)):
            but=discord.ui.Button(label=f'explosion d{explode[i]}',style=discord.ButtonStyle.green)
            async def but_callback(interaction):
                await self.submit(explode[i],interaction)
            but.callback = but_callback
            vu.add_item(but)
        if(self.response_msg==None):
            self.response_msg:discord.Message=await interaction.followup.send(content=f'{interaction.user.mention} {tp}')
        else:
            await self.response_msg.edit(content=f'{interaction.user.mention} {tp}')