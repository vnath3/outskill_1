import json


def read_history(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            # Each line is turned back into a Python Dictionary
            data = json.loads(line)
            print(f"[{data['timestamp']}] User: {data['prompt']}")


def search_history(self, keyword):
        """Finds all previous chats containing a specific word"""
        results = []
        if not os.path.exists(self.history_file):
            return "No history found."

        with open(self.history_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Convert the line back to a dictionary
                entry = json.loads(line)
                # Search in both prompt and response
                if keyword.lower() in entry['prompt'].lower() or \
                   keyword.lower() in entry['response'].lower():
                    results.append(entry)
        
        return results

if __name__ == "__main__":
    # Example usage:
    # read_history("chat_history.jsonl")
    search_history("war")