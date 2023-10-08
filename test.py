import openai
import asyncio

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write me a very long essay!"}],
    max_tokens=1000,
    stream=True
)

for chunk in response:
    print(chunk)


