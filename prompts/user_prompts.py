def evaluator_user_prompt(reply, message, history):
  evaluator_user_prompt = f"Here's the conversation between the User and the Agent:\n\n{history}"
  evaluator_user_prompt += f"Here's the latest message from the User:\n\n{message}"
  evaluator_user_prompt += f"Here's the latest response from the Agent:\n\n{reply}"
  evaluator_user_prompt += "Please evaluate the response, replying with wether it is acceptable plus your feedback."

  return evaluator_user_prompt