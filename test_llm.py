import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

msg = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=50,
    messages=[{"role": "user", "content": "Say 'API key works!' and nothing else."}],
)
print(msg.content[0].text)