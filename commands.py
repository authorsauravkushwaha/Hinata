from ollama_client import ask_ollama


def handle_command(user_input):
    command = user_input.lower().strip()

    # Fast, deterministic commands
    if command in ["hello", "hi", "hey"]:
        return "Hello! How can I help?"

    if "how are you" in command:
        return "I'm running normally and ready to help."

    if command == "help":
        return "You can say hello, ask how I am, or ask me a question."

    # Unknown input → local Ollama model
    prompt = f"""
You are Hinata, a helpful personal desktop assistant.

Rules:
- Be concise and professional.
- Do not claim to have performed an action unless you actually did it.
- If the user asks for something Hinata cannot currently do, say so clearly.
- Answer the user's question directly.

User: {user_input}

Hinata:
"""

    return ask_ollama(prompt)