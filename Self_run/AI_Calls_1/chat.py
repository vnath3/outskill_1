import os
from dotenv import load_dotenv

# Import all your specialists
from history_manager import HistoryManager
from groq_manager import GorqManager
from ai_service import AIService

def main():
    load_dotenv()
    
    # 1. Initialize the low-level workers
    history = HistoryManager("ai_memory.jsonl")
    groq_client = GorqManager(os.getenv("GROQ_API_KEY"))

    # 2. Initialize the high-level service
    # We "inject" the workers into the service
    chat_bot = AIService(groq_client, history)

    # 3. Run the task
    while True:
        query = input("\nAsk me anything (or type 'quit'): ")
        if query.lower() == 'quit':
            break
            
        result = chat_bot.ask(query)
        print(f"\nResult: {result}")

if __name__ == "__main__":
    main()