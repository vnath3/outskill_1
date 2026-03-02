import os
import json
from groq import Groq  # You need to install this: pip install groq
from dotenv import load_dotenv
import datetime
import HistoryManager


class GorqManager:
    def __init__(self, api_key, history_handler: HistoryManager):
        self.__api_key = api_key
        self.client = Groq(api_key=self.__api_key)
        self.history = history_handler  # Injecting the history specialist

    def __save_to_history(self, chat_entry):
        """
        Appends a single JSON object to the end of the file.
        This is memory-efficient for large files.
        """
        # Mode 'a' (Append) opens the file and moves the cursor to the end.
        # It does NOT read the existing content.
        with open(self.history_file, mode='a', encoding='utf-8') as f:
            # We convert the dict to a string and add a newline (\n)
            json_record = json.dumps(chat_entry)
            f.write(json_record + "\n")

    def call_api(self, role, content):
        # 2. Prepare the Payload
        payload = {
            "model": "llama-3.3-70b-versatile",
            "temperature": 0.7,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": role, "content": content}
            ]
        }

        # 3. Get the actual response
        completion = self.client.chat.completions.create(**payload)
        response_text = completion.choices[0].message.content

        # 4. Log the interaction
        log_entry = {
            "timestamp": str(datetime.datetime.now()),
            "prompt": content,
            "response": response_text,
            "usage": {
                "prompt_tokens": completion.usage.prompt_tokens,
                "completion_tokens": completion.usage.completion_tokens,
                "total_tokens": completion.usage.total_tokens
            }
        }
        self.__save_to_history(log_entry)
        return response_text


if __name__ == "__main__":
    load_dotenv()
    # Initialize the specialist first
    my_history = HistoryManager("./my_ai_logs.jsonl")

    matches = my_history.search("Dependency")
    print(f"Found {len(matches)} mentions in history.")
    
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        manager = GorqManager(api_key, my_history)
        response = manager.call_api(
            "user", "What is Dependency Injection?")
        print("Response:", response)
    else:
        print("Please set your GROQ_API_KEY environment variable.")

    # 2. Search (Using the specialist directly)
    matches = my_history.search("Dependency")
    print(f"Found {len(matches)} mentions in history.")
