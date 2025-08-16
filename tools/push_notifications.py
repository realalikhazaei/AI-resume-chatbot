import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)
PUSHBULLET_TOKEN = os.getenv("PUSHBULLET_TOKEN")
PUSHBULLET_URL = os.getenv("PUSHBULLET_URL")


def push(message):
  print(f"Pushing message: {message}")
  headers = {"Access-Token": PUSHBULLET_TOKEN}
  body = {"type": "note", "title": "Chatbot Agent", "body": message}
  requests.post(url=PUSHBULLET_URL, data=body, headers=headers)
