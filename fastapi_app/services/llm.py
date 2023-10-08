import openai
import os

# from shared.config import *

openai.api_key = os.getenv("openai_key")



async def generate_sentence(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        stream=True
    )
    for chunk in response:
        yield chunk["choices"][0]["delta"].get("content", "")

    # for i in range(5): 
    #     char = chr(97 + i)
    #     yield char + "\n"
    #     await asyncio.sleep(0.5)