import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

@bot.event
async def on_ready():
    print(f'Bot successfully logged in as {bot.user}')
    print(f'Bot ID: {bot.user.id}')
    print(f'Connected to {len(bot.guilds)} server(s)')
    print('━' * 50)
    
    activity = discord.Game(name="League of Legends")
    
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Custom activity successfully set!')
    print(f'Bot is now online and ready!')
    
    # Sync slash commands automatically (Global sync can take up to 1 hour)
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} slash command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')