import os

import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")


def generate_response(text, emotion, action):
    prompt = f"""You are EVA, an empathetic voice assistant.
User emotion: {emotion}
Response style: {action}
User said: {text}
Respond naturally and concisely. Do not mention internal emotion detection or policy rules."""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        generated = data.get("response", "").strip()
        if generated:
            return generated
    except (requests.RequestException, ValueError):
        pass

    fallbacks = {
        "sad": "I'm here with you. Take a breath, and tell me what is bothering you.",
        "angry": "I understand that this is frustrating. Let's slow down and work through it together.",
        "excited": "That sounds exciting! Tell me more about it.",
        "neutral": "I'm listening. How can I help?",
    }
    return fallbacks.get(emotion, fallbacks["neutral"])
