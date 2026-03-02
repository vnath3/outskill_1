import json
import os

class HistoryManager:
    def __init__(self, filename="chat_history.jsonl"):
        self.filename = filename

    def add_entry(self, entry_dict):
        """Append a single record to the ledger."""
        with open(self.filename, mode='a', encoding='utf-8') as f:
            f.write(json.dumps(entry_dict) + "\n")

    def search(self, keyword):
        """Search the ledger line-by-line."""
        results = []
        if not os.path.exists(self.filename):
            return results
        
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                if keyword.lower() in str(data).lower():
                    results.append(data)
        return results