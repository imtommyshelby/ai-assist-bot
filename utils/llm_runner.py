import requests

def generate_response(prompt: str, model: str = "mistral") -> str:
    try:
        response = requests.post(
            "http://localhost:11600/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "").strip()
    except Exception as e:
        return f"❌ Failed to generate response: {e}"
