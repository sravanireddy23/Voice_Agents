
# 30 Days of AI Voice Agents | Day 25: Agent Special Skill 1

## Overview
Day 25 focuses on **adding a special skill** to the voice agent. Special skills extend the agent's capabilities beyond regular conversation, such as:

- Searching the web
- Getting the latest weather
- Fetching current news
- Performing calculations or translations
- Any other creative functionality you can think of

This makes the agent more **interactive and useful**.

---

## Features
- **Custom Skill Integration**: Add unique functions to the agent.
- **Enhanced Conversational Abilities**: Agent can perform tasks or provide information beyond regular chat.
- **Function Calling with LLM**: Use Gemini API’s function calling to invoke skills automatically based on user queries.
- **Dynamic Responses**: Agent responds with information or performs the task in real-time.

---

## How It Works
1. Define a **special skill function** in your server:
```python
def get_weather(city: str):
    # Call a weather API and return current weather
    return f"The weather in {city} is sunny, 28°C."
````

2. Configure the LLM to **call functions** automatically based on user input:

```python
from gemini import GeminiClient
client = GeminiClient(api_key="your_gemini_key")
response = client.generate(
    prompt="What's the weather in Paris?",
    functions=[get_weather]
)
```

3. The LLM detects when a skill should be used and calls the appropriate function.
4. The agent returns the function result as part of the conversation.

---

## Usage

1. Add your API keys or necessary credentials for the skill (e.g., weather API, news API).
2. Define the special skill functions on the server.
3. Include them in the **Gemini function-calling setup**.
4. Interact with the agent and ask questions that trigger the skill.
5. Observe the agent responding with the enhanced functionality.

---

## Notes

* Special skills can be **expanded indefinitely**—any API or logic can be integrated.
* Function-calling with Gemini allows the LLM to **invoke the skill automatically**.
* Make sure to **handle errors gracefully** in skill functions to maintain a smooth experience.

---

## Resources

* [Gemini API Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?example=weather#automatic_function_calling_python_only)
* [Web Search Skill Example](https://docs.tavily.com/documentation/quickstart)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student


