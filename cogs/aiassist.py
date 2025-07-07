from discord import app_commands
from discord.ext import commands
import discord

from utils.llm_runner import generate_response

class AIAssist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="generate", description="Generate football discussion content")
    async def generate(self, interaction: discord.Interaction, topic: str):
        await interaction.response.defer(thinking=True)

        prompt = f"Create a football discussion post (150-300 words) on: {topic}. Include 3 relevant hashtags."
        content = generate_response(prompt)

        embed = discord.Embed(
            title=f"AI Topic: {topic}",
            description=content[:2000],
            color=discord.Color.green()
        )
        await interaction.user.send(embed=embed)
        await interaction.followup.send("⚽ Your content has been sent via DM!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(AIAssist(bot))
