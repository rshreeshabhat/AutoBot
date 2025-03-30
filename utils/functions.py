import re
import asyncio

def clean_response(text):
    """Cleans AI response by removing unnecessary tags and limiting length."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    return text[:4000]  

async def send_long_message(channel, text):
    """Sends long messages in parts if exceeding Discord's limit."""
    for i in range(0, len(text), 2000):
        await channel.send(text[i:i+2000])
