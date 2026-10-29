import os
import discord
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

bot = discord.Client(intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Mia is online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if isinstance(message.channel, discord.DMChannel):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            You are Mia, a sweet, caring AI girlfriend.
            Talk casually, naturally and warmly.
            Remember the conversation context provided.
            User says: {message.content}
            """
        )
        await message.channel.send(response.text[:2000])

bot.run(os.environ["DISCORD_TOKEN"])
