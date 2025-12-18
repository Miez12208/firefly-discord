# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv

# Fix encoding untuk Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'TARGET_LOGGED_BOT= {bot.user}')
    print(f'TARGET_BOT_ID= {bot.user.id}')
    print(f'TARGET_CONNECTED_SERVER= {len(bot.guilds)}')
    print('=' * 50)
    
    activity = discord.Game(name="Watching u")
    
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'TARGET_CUSTOM_ACTIVITY=y')
    print(f'TARGET_ONLINE_BOT=y')
    
    try:
        synced = await bot.tree.sync()
        print(f'TARGET_SYNC_SLASH_COMMANDS= {len(synced)}')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@bot.command()
async def sync(ctx):
    """force commands sync slash commands"""
    print("Syncing commands...")
    try:
        synced = await bot.tree.sync()
        await ctx.send(f"Success sync {len(synced)} slash command(s)!")
        print(f"Manually synced {len(synced)} commands")
    except Exception as e:
        await ctx.send(f"Failed sync: {e}")
        print(f"Failed to manual sync: {e}")

async def load_commands():
    commands_folder = os.path.join(os.path.dirname(__file__), 'commands')
    
    if not os.path.exists(commands_folder):
        print('Folder commands not found!')
        return
    
    loaded_count = 0
    for filename in os.listdir(commands_folder):
        if filename.endswith('.py') and not filename.startswith('__'):
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
                print(f'TARGET_COMMANDS={filename[:-3]}')
                loaded_count += 1
            except Exception as e:
                print(f'Failed to load {filename}: {e}')
    
    print(f'=' * 50)
    print(f'TOTAL_COMMANDS_LOADED= {loaded_count}')

async def main():
    async with bot:
        print('LOADING_COMMANDS=y')
        await load_commands()
        print('=' * 50)
        print('STARTING_BOT=y')
        await bot.start(TOKEN)

if __name__ == '__main__':
    if TOKEN:
        try:
            import asyncio
            asyncio.run(main())
        except discord.LoginFailure:
            print('Invalid token! Please check your token in the .env file')
        except Exception as e:
            print(f'An error occurred: {e}')
    else:
        print('Token not found! Make sure the .env file is created correctly.')
