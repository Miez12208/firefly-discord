import discord
from discord import app_commands
from discord.ext import commands
import random

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="ping", description="Check bot latency and status")
    async def ping(self, interaction: discord.Interaction):
        """Command to check bot latency with attractive display"""
        
        # Calculate latency
        latency = round(self.bot.latency * 1000)
        
        # Generate random color for embed
        color = random.randint(0x000000, 0xFFFFFF)
        
        # Determine status emoji based on latency
        if latency < 100:
            status_emoji = "🟢"
            status_text = "Excellent"
        elif latency < 200:
            status_emoji = "🟡"
            status_text = "Good"
        elif latency < 300:
            status_emoji = "🟠"
            status_text = "Fair"
        else:
            status_emoji = "🔴"
            status_text = "Poor"
        
        # Create attractive embed
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"**Bot is running smoothly!**",
            color=color,
            timestamp=interaction.created_at
        )
        
        # Add field for latency
        embed.add_field(
            name=f"{status_emoji} Latency",
            value=f"```yaml\n{latency}ms\n```",
            inline=True
        )
        
        # Add field for status
        embed.add_field(
            name="📊 Status",
            value=f"```\n{status_text}\n```",
            inline=True
        )
        
        # Add field for server count
        embed.add_field(
            name="🌐 Servers",
            value=f"```\n{len(self.bot.guilds)}\n```",
            inline=True
        )
        
        # Add footer
        embed.set_footer(
            text=f"Requested by {interaction.user.name}",
            icon_url=interaction.user.display_avatar.url
        )
        
        # Add thumbnail (optional - can be replaced with bot logo)
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))
