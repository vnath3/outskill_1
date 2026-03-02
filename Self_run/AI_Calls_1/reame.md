# Modular AI Caching System

A professional-grade Python implementation of an AI agent with a **Local Semantic Cache**. This system separates concerns into four distinct layers to ensure high scalability, cost-efficiency, and "plug-and-play" model swapping.

---

## 🛠️ System Architecture

The project follows the **Service Layer Pattern** and uses **Dependency Injection** to manage interactions between the local filesystem and the Cloud AI.

### **1. Class Responsibilities**

| Class | Role | Responsibility |
| :--- | :--- | :--- |
| **`HistoryManager`** | The Librarian | Manages the `.jsonl` database. Normalizes queries and performs lookups to avoid redundant API calls. |
| **`GorqManager`** | The Messenger | A dedicated wrapper for the Groq API. Handles raw communication with Llama models. |
| **`AIService`** | The Brain | The orchestrator of logic. It decides whether to serve a response from the cache or fetch a new one from the cloud. |
| **`Orchestrator`** | The Owner | The entry point. It initializes all specialists and starts the execution loop. |

---

## 🔄 Execution Flow (The Call Chain)

When a user submits a query, the following sequence is triggered:

1. **Initialization**: `Orchestrator` creates instances of the Librarian and Messenger, then "injects" them into the `AIService`.
2. **Cache Check**: `AIService` asks `HistoryManager` to look for a normalized match of the prompt in `ai_memory.jsonl`.
3. **Decision**:
   - **Cache Hit**: If a match is found, the stored response is returned immediately ($0.00 cost).
   - **Cache Miss**: If no match exists, `AIService` triggers `GorqManager`.
4. **API Call**: `GorqManager` fetches a response from the Groq Cloud (Llama 3.3).
5. **Persistence**: `AIService` tells `HistoryManager` to append the new result to the log for future use.
6. **Output**: The final result is returned to the `Orchestrator` for display.



---

## 🚀 Key Features

* **Cost Efficiency**: Reduces API costs by 100% for repeated or similar queries.
* **Normalization**: Uses RegEx to ensure "What is AI?" and "what is ai" match the same cache entry.
* **Memory Efficiency**: Uses **JSON Lines (.jsonl)** format, allowing the history to grow to millions of entries without slowing down your RAM.
* **Decoupled Design**: Easily swap Groq for Gemini or OpenAI by simply creating a new "Messenger" class—no changes to the logic or history layers required.

---

## 📂 File Structure

```text
.
├── .env                # API Keys and Secrets
├── history_manager.py  # Data Access Layer (Librarian)
├── groq_manager.py     # API Wrapper (Messenger)
├── ai_service.py       # Logic Layer (The Brain)
└── orchestrator.py     # Main Entry Point

⚙️ Setup
Install dependencies: pip install groq python-dotenv
Add your key to .env: GROQ_API_KEY=your_key_here
Run the system: python orchestrator.py