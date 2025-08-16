import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts.system_prompts import system_prompt

load_dotenv(override=True)
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=GEMINI_API_KEY)


def rerun(reply, message, history, feedback):
  updated_system_prompt = system_prompt
  updated_system_prompt += (
    "\n\n## Previous answer rejected\nYou just tried to reply, but the quality control rejected your reply\n"
  )
  updated_system_prompt += f"## Yor attempted answer:\n{reply}\n\n"
  updated_system_prompt += f"## Reason for rejection:\n{feedback}\n\n"

  messages = [{"role": "system", "content": updated_system_prompt}] + history + [{"role": "user", "content": message}]
  responses = gemini.chat.completions.create(model="gemini-2.0-flash", messages=messages)
  return responses.choices[0].message.content
