import json
import os
import re


class HistoryManager:
    def __init__(self, filename="ai_memory.jsonl"):
        self.filename = filename

    def _normalize(self, text):
        """Cleans text for fair comparison: lowercase, no punctuation, no extra spaces."""
        text = text.lower().strip()
        # This removes everything except letters, numbers, and spaces
        return re.sub(r'[^\w\s]', '', text)

    # --- THIS WAS LIKELY MISSING ---
    def add_entry(self, entry_dict):
        """Appends a new record to the .jsonl ledger."""
        with open(self.filename, mode='a', encoding='utf-8') as f:
            f.write(json.dumps(entry_dict) + "\n")

    def find_cached_answer(self, user_query):
        """Looks for an exact (normalized) match of the question."""
        if not os.path.exists(self.filename):
            return None

        normalized_query = self._normalize(user_query)

        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    # We compare the normalized version of the stored prompt to our query
                    if self._normalize(data.get('prompt', '')) == normalized_query:
                        return data.get('response')
                except json.JSONDecodeError:
                    continue
        return None
