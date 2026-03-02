from groq import Groq


class GorqManager:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def call_api(self, role, content):
        """Executes the raw API call to Llama."""
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": role, "content": content}
            ]
        }

        completion = self.client.chat.completions.create(**payload)
        return completion
