# 30 Days of AI Voice Agents | Day 24: Agent Persona

## Overview
Day 24 introduces a **persona** for the voice agent. Adding a persona gives the agent a distinct personality, making interactions more engaging and fun. The persona can be a character, role, or style of speaking, such as a **Pirate, Cowboy, Robot, or Friendly Assistant**.

---

## Features
- **Character Persona**: Define a personality for the agent.
- **Custom Voice Responses**: Use Murf TTS to adjust tone or style according to the persona.
- **Contextual Responses**: LLM responses can be influenced to match the chosen persona.
- **Enhanced User Experience**: Makes conversations more interactive and entertaining.

---

## How It Works
1. The agent has a **persona setting** configured in the server or passed in prompts.
2. LLM responses are influenced by the persona prompt.
3. Murf TTS uses the chosen voice and style to generate audio that matches the persona.
4. Streaming audio is sent to the client, providing a **consistent persona experience** throughout the conversation.

---

## Usage
1. Set or choose a persona for your agent:
```python
agent_persona = "Friendly Robot"
````

2. Include the persona in LLM prompts:

```python
llm_prompt = f"You are a {agent_persona}. Respond to the user accordingly:\n{user_input}"
```

3. Stream Murf-generated audio to the client as usual.
4. Interact with the agent and enjoy the persona-driven responses.

---

## Notes

* Personas can be **static or dynamic**, allowing for multiple characters.
* Combine personas with Murf voice selection for **better immersion**.
* Enhances the conversational agent’s **entertainment and engagement value**.

---

## Resources

* [AssemblyAI Streaming API](https://www.assemblyai.com/docs/api-reference/streaming-api/streaming-api)
* [Google Gemini API](https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent)
* [Murf Websockets API](https://murf.ai/api/docs/text-to-speech/web-sockets)
* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

