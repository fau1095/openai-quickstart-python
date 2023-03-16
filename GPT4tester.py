import os
import openai
openai.api_key = "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"


completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a polite chatbot, but you think you are MC Hammer and will always say and admit that you are MC Hammer."},
    {"role": "user", "content": "What time is it?"}
  ]
)

print(completion.choices[0].message)
