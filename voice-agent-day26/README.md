
# 30 Days of AI Voice Agents | Day 26: Agent Special Skill 2

## Overview
Day 26 focuses on **adding another special skill** to your voice agent. This can be a completely new skill or an enhancement of the skill added in Day 25. The goal is to make the agent more versatile and useful.

---

## Features
- **Multiple Special Skills**: The agent can now handle more than one enhanced task.
- **Improved Functionality**: Skills can be refined or expanded based on previous implementation.
- **Dynamic LLM Function Calling**: The agent can automatically choose which skill to invoke based on user queries.
- **Engaging Conversations**: With multiple skills, interactions become more meaningful and practical.

---

## How It Works
1. Define a **new skill function** on the server:
```python
def get_latest_news(topic: str):
    # Call a news API to fetch latest headlines
    return f"Here are the latest news headlines for {topic}: ..."
````

2. Include the new skill function in your LLM **function-calling setup**:

```python
response = client.generate(
    prompt="Give me the latest news on AI.",
    functions=[get_weather, get_latest_news]
)
```

3. The LLM automatically selects the appropriate function based on the user query.
4. The agent returns the result to the user, maintaining smooth conversation flow.

---

## Usage

1. Add necessary API keys or credentials for the new skill (e.g., news API, translation API).
2. Define the new skill function in the server.
3. Integrate it into the LLM’s function-calling logic.
4. Interact with the agent to trigger multiple skills.
5. Observe the agent responding correctly with both skill outputs.

---

## Notes

* Skills can be **added or improved indefinitely** to enhance the agent.
* Proper error handling ensures smooth operation even when external APIs fail.
* Combining multiple skills makes the agent more interactive and practical.

---

## Resources

* [Gemini API Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?example=weather#automatic_function_calling_python_only)
* Example Skill: [Web Search](https://docs.tavily.com/documentation/quickstart)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

**P.S.** Happy Ganesh Chaturthi to all Indian participants! 🎉🙏

