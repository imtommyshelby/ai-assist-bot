# cogs/aiassist.py

from discord import app_commands
from discord.ext import commands
import discord

from utils.llm_runner import generate_response
from utils.news_fetcher import fetch_all_sources  # 🗞 Pull latest news

class AIAssist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="generate", description="Generate football discussion content")
    @app_commands.describe(topic="Football topic you want AI to discuss")
    async def generate(self, interaction: discord.Interaction, topic: str):
        await interaction.response.defer(thinking=True)

        try:
            # 📰 Get real-time football news
            news_snippets = fetch_all_sources()

            # 🧠 Craft AI prompt using latest news
            prompt = f"""
Create a football discussion post (150-300 words) on the topic: "{topic}".
Here are recent headlines you should include:
{news_snippets}

Add 3 relevant hashtags at the end.
"""

            # 🧪 Generate content
            content = generate_response(prompt)

            # 📦 Build and send the embed
            embed = discord.Embed(
                title=f"⚽ AI Topic: {topic}",
                description=content[:2000],
                color=discord.Color.green()
            )

            await interaction.user.send(embed=embed)
            await interaction.followup.send("✅ Your football content has been sent via DM!", ephemeral=True)

        except Exception as e:
            await interaction.followup.send(f"❌ Error generating content: {e}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(AIAssist(bot))
