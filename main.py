import discord 
import requests
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks


APIkey = "api-xxxx-xxxx"
token = "yourbottoken"

client = commands.Bot(command_prefix='123456789qwertyuiopasdfghjklzxcvbnm', intents= discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print('connected!')
    try:
        synced = await client.tree.sync()
        print(f'synced {len(synced)} command(s)')
    except Exception as e:
        print(e)
        
        
@client.tree.command(name='altening',
                    description="by @fantia#2023"                  
)
async def alt(interaction: discord.Interaction):
    r = requests.get(f"http://api.thealtening.com/v2/generate?key={APIkey}")
    token = r.json()["token"]
    username = r.json()["username"]
    expires = r.json()["expires"]
    expires = expires.replace("T", " ")
    char = "."
    result = expires[:expires.index(char)] if char in expires else expires
    embed = discord.Embed(title="Altening Token", color=0x1ab725)
    embed.add_field(name="Token", value=token, inline=False)
    embed.add_field(name="Username", value=username, inline=False)
    embed.set_footer(text=f"expires {result}")
    await interaction.response.send_message(embed=embed, ephemeral=True)
    
client.run(token)
