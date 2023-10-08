import openai
import os

openai.api_key = os.getenv("openai_key")


async def generate_sentence(prompt: str, system: str, history: list):
    user_msg = {"role": "user", "content": prompt}
    if history is not None:
        history.append(user_msg)
    else:
        history = [user_msg]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history,
        max_tokens=500,
        stream=True
    )
    for chunk in response:
        yield chunk["choices"][0]["delta"].get("content", "")