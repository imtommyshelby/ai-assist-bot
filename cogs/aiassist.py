# cogs/aiassist.py

from discord import app_commands
from discord.ext import commands
import discord

from utils.llm_runner import generate_response
from utils.news_fetcher.filter import fetch_relevant_news  # ✅ Pull only filtered headlines
from utils.prompt_template import build_prompt             # ✅ CBS Golazo-style personality prompt

class AIAssist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="generate", description="Generate football discussion content")
    @app_commands.describe(topic="Football topic you want AI to discuss")
    async def generate(self, interaction: discord.Interaction, topic: str):
        await interaction.response.defer(thinking=True)

        try:
            # 🗞 1. Fetch news filtered to the user's topic
            news_snippets = fetch_relevant_news(topic)

            # 🧠 2. Generate human-style, intelligent prompt
            prompt = build_prompt(topic, news_snippets)

            # 🤖 3. Get response from local LLM
            content = generate_response(prompt)

            # 📦 4. Build the Discord embed
            embed = discord.Embed(
                title=f"⚽ AI Topic: {topic}",
                description=content[:2000],  # Discord message cap
                color=discord.Color.green()
            )

            # 📬 5. Send to user in DMs
            await interaction.user.send(embed=embed)

            # ✅ 6. Confirm in the channel
            await interaction.followup.send("✅ Your football content has been sent via DM!", ephemeral=True)

        except Exception as e:
            await interaction.followup.send(f"❌ Error generating content: {e}", ephemeral=True)

# 🧩 Required for dynamic cog loading
async def setup(bot):
    await bot.add_cog(AIAssist(bot))
