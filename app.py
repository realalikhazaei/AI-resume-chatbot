import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from prompts.system_prompts import system_prompt
from tools.rerun import rerun
from tools.evaluate import evaluate
from tools.tool_handler import handle_tool_calls
from tools.record_user_details import record_user_details_json
from tools.record_unknown_question import record_unknown_question_json

load_dotenv(override=True)

OWNER_NAME = os.getenv("OWNER_NAME")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PUSHBULLET_URL = os.getenv("PUSHBULLET_URL")
PUSHBULLET_TOKEN = os.getenv("PUSHBULLET_TOKEN")

gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=GEMINI_API_KEY)

tools = [
  {"type": "function", "function": record_user_details_json},
  {"type": "function", "function": record_unknown_question_json},
]


def chat(message, history):
  messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
  done = False

  while not done:
    response = gemini.chat.completions.create(model="gemini-2.0-flash", messages=messages, tools=tools)

    if response.choices[0].finish_reason == "tool_calls":
      message = response.choices[0].message
      tool_calls = message.tool_calls
      results = handle_tool_calls(tool_calls)
      messages.append(message)
      messages.extend(results)
    else:
      done = True

  reply = response.choices[0].message.content
  evaluation = evaluate(reply, message, history)

  if not evaluation.is_acceptable:
    print("Failed evaluation - retrying")
    print(evaluation.feedback)
    reply = rerun(reply, message, history, evaluation.feedback)

  return reply


gr.ChatInterface(
  chat,
  type="messages",
  flagging_mode="manual",
  flagging_options=["Like", "Spam", "Inappropriate", "Other"],
).launch()
