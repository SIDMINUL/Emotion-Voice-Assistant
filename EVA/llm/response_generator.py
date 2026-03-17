import requests

def generate_response(text, emotion, action):

    prompt = f"""
User emotion: {emotion}
Response style: {action}

User said: {text}

Respond empathetically.
"""

    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = r.json()

    # Debug print (optional)
    #print("LLM Response:", data)

    return data.get("response", "Sorry, I couldn't generate a response.")