import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from prompts.system_prompts import evaluator_system_prompt
from prompts.user_prompts import evaluator_user_prompt

load_dotenv(override=True)
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=GEMINI_API_KEY)


class Evaluation(BaseModel):
  is_acceptable: bool
  feedback: str


def evaluate(reply, message, history) -> Evaluation:
  messages = [{"role": "system", "content": evaluator_system_prompt}] + [
    {"role": "user", "content": evaluator_user_prompt(reply, message, history)}
  ]
  response = gemini.beta.chat.completions.parse(model="gemini-2.5-flash", messages=messages, response_format=Evaluation)
  return response.choices[0].message.parsed
