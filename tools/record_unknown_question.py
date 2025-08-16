from tools.push_notifications import push


def record_unknown_question_tool(question):
  push(f"Recording a question I couldn't answer:\n{question}")
  return {"recorded": True}


record_unknown_question_json = {
  "name": "record_unknown_question_tool",
  "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
  "parameters": {
    "type": "object",
    "properties": {
      "question": {
        "type": "string",
        "description": "This is the question I couldn't answer",
      }
    },
    "required": ["question"],
    "additionalProperties": False,
  },
}
