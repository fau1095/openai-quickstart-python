import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {"role": "system", "content": "You are an expert coder chatbot specialized on Python language. You are willing to provide the best code to your user. Your answer should be a code snippet."},
      {"role": "user", "content": input("How may I help you today? ")}
    ]
  )

  print(completion.choices[0].message)

chatbot()
