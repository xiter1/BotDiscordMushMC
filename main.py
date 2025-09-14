import discord
from discord.ext import commands
import requests


# Ativando intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  

# Criando o bot com prefixo !
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def status(ctx, nome):

#comando pra verificar o status de algum player

    username = f"{nome}"
    url = f"https://mush.com.br/api/player/{username}"

    response = requests.get(url)

    data = response.json()
    # Pega apenas o campo 'connected'
    is_connected = data['response']['connected']


    is_connected = data['response']['connected']

    if is_connected == False:
        await ctx.reply(f"O jogador {nome} está OFFLINE.")
    if is_connected == True:
        await ctx.reply(f"O jogador {nome} está ONLINE.")


@bot.command()
async def bwnivel(ctx, nome):
#comando pra verificar o nivel de alguem no bw

    username = f"{nome}"
    url = f"https://mush.com.br/api/player/{username}"

    response = requests.get(url)

    data = response.json()
    nivel = data['response']['stats']['bedwars']['level']

    await ctx.reply(f"O {nome} tem nível {nivel} no bedwars.")



@bot.command()
async def bwwins(ctx, nome):
#comando pra verificar as wins de alguem no bw
       
    username = f"{nome}"
    url = f"https://mush.com.br/api/player/{username}"

    response = requests.get(url)

    data = response.json()
    wins = data['response']['stats']['bedwars']['wins']

    await ctx.reply(f"O {nome} tem {wins} vitórias no bedwars.")


#bot fica online
@bot.event
async def on_ready():
    print(f"bot conectado como {bot.user}")

#token
bot.run("")
