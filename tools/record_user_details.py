from tools.push_notifications import push


def record_user_details_tool(email, name="Name not provided", notes="not provided"):
  push(f"Recording interested user to connect {name} with the email {email} and notes: {notes}")
  return {"recorded": True}


record_user_details_json = {
  "name": "record_user_details_tool",
  "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
  "parameters": {
    "type": "object",
    "properties": {
      "email": {"type": "string", "description": "This is the user's email"},
      "name": {
        "type": "string",
        "description": "This is the user's name, in case of being provided",
      },
      "notes": {
        "type": "string",
        "description": "Any additional information about the conversation that's worth recording to give context",
      },
    },
    "required": ["email"],
    "additionalFields": False,
  },
}
