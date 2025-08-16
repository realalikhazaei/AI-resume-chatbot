import json
from tools.record_user_details import record_user_details_tool
from tools.record_unknown_question import record_unknown_question_tool


def handle_tool_calls(tool_calls):
  print("Calling tools", tool_calls)
  results = []
  for tool_call in tool_calls:
    tool_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    tool = globals().get(tool_name)
    result = tool(**arguments) if tool else {}
    results.append(
      {
        "role": "tool",
        "content": json.dumps(result),
        "tool_call_id": tool_call.id,
      }
    )

  return results
