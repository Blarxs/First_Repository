import discord
from discord.ext import commands
import random
import os
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='|', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

#@bot.command()
#async def mem(ctx):
    #img_name = random.choice(os.listdir('images'))
    ## ¡Y así es como se puede sustituir el nombre del fichero desde una variable!
    #with open(f'images/{img_name}', 'rb') as f:
        #picture = discord.File(f)
        #await ctx.send(file=picture)

@bot.command("apple1")
async def apple1(ctx):
    with open('images/IMG1.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command("apple2")
async def apple2(ctx):
    with open('images/IMG2.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command("apple3")
async def apple3(ctx):
    with open('images/IMG3.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command("iOS26")
async def iOS26(ctx):
    with open('images/iOS26.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def codemem1(ctx):
    with open('images/meme1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def codemem2(ctx):
    with open('images/meme2.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def codemem3(ctx):
    with open('images/meme3.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_cat_image_url():    
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url)
    data = res.json()
    return data[0]['url']


@bot.command('Kit')
async def Kit(ctx):
    '''Una vez que llamamos al comando cat, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_cat_image_url()
    await ctx.send(image_url)

class MenuView(discord.ui.View):
    @discord.ui.button(label="Opción 1", style=discord.ButtonStyle.primary, row=0)
    async def option1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Elegiste la Opción 1", ephemeral=True)

    @discord.ui.button(label="Opción 2", style=discord.ButtonStyle.success, row=1)
    async def option2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Elegiste la Opción 2", ephemeral=True)

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.danger, row=2)
    async def exit(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("¡Menú cerrado!", ephemeral=True)
        self.stop()

@bot.command(name="menu")
async def menu(ctx):
    view = MenuView()
    await ctx.send("Elige una opción del menú:", view=view)

bot.run("TOKEN")
