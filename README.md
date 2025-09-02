---
title: AI-resume-chatbot
app_file: app.py
sdk: gradio
sdk_version: 5.42.0
python_version: "3.12.0"
---

# 🤖 AI Resume Chatbot

An interactive AI-powered chatbot which can link to a professional resume (mine is available in this repo) and chat with clients, future co-workers and potential employers on behalf of you, in a conversational format. The chatbot leverages OpenAI and Google AI APIs to provide intelligent responses. The project is deployed as a Hugging Face Space and features a CI/CD pipeline using GitHub Actions for automated updates.

## Important
Make sure to install the dependencies only for Python v3.12. Also change the resources with your own.

## Key Features:

* Conversational Resume: Allows users to ask questions about my skills, experience, and projects.
* AI Integration: Connected to powerful language models for natural and context-aware conversations.
* Web Interface: Built with Gradio for a simple and intuitive user experience.
* Automated Deployment: CI/CD pipeline with GitHub Actions automatically deploys changes to Hugging Face.
* Pushing Notifications: Uses PushBullet app to send notifications about connection requests and unknown questions.

## Tech Stack:

* Language: Python
* AI Libraries: OpenAI, Google AI
* UI Framework: Gradio
* CI/CD: GitHub Actions
* Deployment: Hugging Face Spaces
* Notifications: PushBullet

## Setup and Installation

1. Clone the master branch from the repository:

```
git clone --branch master https://github.com/realalikhazaei/ai-resume-chatbot
```

2. Create a uv virtual environment and install the required packages (recommended):

```
uv venv --python 3.12
uv pip install -r requirements.txt
```

3. Or install the required Python packages using Pip:

```
pip install -r requirements.txt
```

4. Create a .env file in the root and add your API keys:

```
//Example Variables

OWNER_NAME = <your name>
GEMINI_BASE_URL = https://generativelanguage.googleapis.com/v1beta/openai/
GEMINI_API_KEY = <your google ai api key>
PUSHBULLET_URL = https://api.pushbullet.com/v2/pushes
PUSHBULLET_TOKEN = <your pushbullet token>
```

5. Run the application:

```
//With uv

uv run app.py
```

```
//With Python itself

python app.py
```
