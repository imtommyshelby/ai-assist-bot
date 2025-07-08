# cogs/aiassist.py

from discord import app_commands
from discord.ext import commands
import discord

from utils.llm_runner import generate_response
from utils.news_fetcher import fetch_all_sources  # 🗞 Pull latest news
from utils.prompt_template import build_prompt     # 🔥 Custom Golazo-style prompt

class AIAssist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="generate", description="Generate football discussion content")
    @app_commands.describe(topic="Football topic you want AI to discuss")
    async def generate(self, interaction: discord.Interaction, topic: str):
        await interaction.response.defer(thinking=True)

        try:
            # 🗞 Fetch live football news headlines from multiple sources
            news_snippets = fetch_all_sources()

            # 🧠 Build Golazo-style human prompt using personality + news
            prompt = build_prompt(topic, news_snippets)

            # 💡 Generate LLM-based discussion using your local model
            content = generate_response(prompt)

            # 📦 Format into a Discord embed
            embed = discord.Embed(
                title=f"⚽ AI Topic: {topic}",
                description=content[:2000],  # Discord's message limit
                color=discord.Color.green()
            )

            # 📬 Send response to user via DM
            await interaction.user.send(embed=embed)

            # ✅ Notify in channel
            await interaction.followup.send("✅ Your football content has been sent via DM!", ephemeral=True)

        except Exception as e:
            await interaction.followup.send(f"❌ Error generating content: {e}", ephemeral=True)

# 🧩 Required for dynamic cog loading
async def setup(bot):
    await bot.add_cog(AIAssist(bot))
