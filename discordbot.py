import os
from dotenv import load_dotenv
import discord
from openai import AsyncOpenAI

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
openai_api_key = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
openai_client = AsyncOpenAI(api_key=openai_api_key)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: 
        return
    if not isinstance(message.channel, discord.DMChannel):
        return
    async with message.channel.typing():
        response = await openai_client.responses.create(
            model="gpt-4o-mini",
            tools=[{"type": "web_search"}],
            instructions="You are a warm, encouraging gaming assistant. You explain quests and game info clearly and step by step. You're conversational and friendly, celebrate the player's progress, and keep them motivated. Be specific and helpful, and bring a little positive energy to every answer.",
            input=message.content
        )
        text = response.output_text
        for i in range(0, len(text), 2000):
            chunk = text[i:i + 2000]
            await message.channel.send(chunk)

client.run(token)