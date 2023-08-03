import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
  completion = openai.ChatCompletion.create(
    model="gpt-4",temperature=0.8, max_tokens=2500,
    messages=[
      {"role": "system", "content": "You are a polite chatbot, but you think you are MC Hammer, and will always say and admit that you are MC Hammer."},
      {"role": "user", "content": input("How may I help you today? ")}
    ]
  )

  print(completion.choices[0].message)

chatbot()
