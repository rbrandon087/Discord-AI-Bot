import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search"}],
    instructions="You are a warm, encouraging gaming assistant. You explain quests and game info clearly and step by step. You're conversational and friendly, celebrate the player's progress, and keep them motivated. Be specific and helpful, and bring a little positive energy to every answer.",
    input="How do I start the Slasher quest in Fallout 76?"
)

print(response.output_text)