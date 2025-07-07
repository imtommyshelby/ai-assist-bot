# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix="/", intents=intents)

# Single on_ready event
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is online and slash commands are synced!")

# Proper async main function
async def main():
    async with bot:
        await bot.load_extension("cogs.aiassist")  # Load your cog correctly
        await bot.start(TOKEN)

# Start the bot
asyncio.run(main())
