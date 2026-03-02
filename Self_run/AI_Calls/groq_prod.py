import os
import json
import datetime
from groq import Groq
from dotenv import load_dotenv

# --- CLASS 1: THE SPECIALIST ---
class HistoryManager:
    def __init__(self, filename="chat_history.jsonl"):
        self.filename = filename

    def add_entry(self, entry_dict):
        with open(self.filename, mode='a', encoding='utf-8') as f:
            f.write(json.dumps(entry_dict) + "\n")

    def search(self, keyword):
        results = []
        if not os.path.exists(self.filename):
            return results
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                if keyword.lower() in str(data).lower():
                    results.append(data)
        return results

# --- CLASS 2: THE AI MANAGER ---
class GorqManager:
    def __init__(self, api_key, history_handler: HistoryManager):
        self.client = Groq(api_key=api_key)
        self.history = history_handler  # Store the specialist

    def call_api(self, role, content):
        payload = {
            "model": "llama-3.3-70b-versatile",
            "temperature": 0.7,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": role, "content": content}
            ]
        }

        completion = self.client.chat.completions.create(**payload)
        response_text = completion.choices[0].message.content

        log_entry = {
            "timestamp": str(datetime.datetime.now()),
            "prompt": content,
            "response": response_text,
            "usage": {
                "total_tokens": completion.usage.total_tokens
            }
        }

        # USE THE SPECIALIST HERE!
        self.history.add_entry(log_entry) 
        
        return response_text

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    load_dotenv()
    
    # 1. Setup the history specialist
    my_history = HistoryManager("my_ai_logs.jsonl")

    # 2. Setup the AI manager with the specialist
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        manager = GorqManager(api_key, my_history)
        
        # 3. Use the system
        response = manager.call_api("user", "Explain Dependency Injection.")
        print("Response received and logged.")

        # 4. Search using the specialist
        matches = my_history.search("Dependency")
        print(f"Found {len(matches)} mentions in history.")