"""
====================================================================
THE AI DATA MASTER WORKBOOK
====================================================================
This script contains all the challenges to practice lists, 
dictionaries, sets, tuples, list comprehensions, and error handling.
====================================================================
"""
from collections import namedtuple
import json

# ==================================================================
# Challenge 1: Basic List Operations (The Prompt Queue)
# ==================================================================
raw_prompts = [" hello ", "What is AI?", "  python  "]

# TODO: Add "Goodbye!" to the end.
# TODO: Insert "SYSTEM: Act as a tutor" at index 0.
# TODO: Remove the 3rd item in the list (index 2).
# TODO: Print the final length.

print("Challenge 1 Result:", raw_prompts)

# ==================================================================
# Challenge 2: List Comprehension (The Text Normalizer)
# ==================================================================
user_inputs = ["  What is AI? ", "python list  ", "  Explain DEEP learning  "]

# TODO: Create 'clean_inputs' where every string is lowercased and stripped.
clean_inputs = []

# TODO: Create 'short_queries' containing only strings from clean_inputs <= 20 characters.
short_queries = []

print("Challenge 2 - Clean Inputs:", clean_inputs)
print("Challenge 2 - Short Queries:", short_queries)

# ==================================================================
# Challenge 3: Advanced Comprehension (The Cost Calculator)
# ==================================================================
token_counts = [45, 200, 15, 500, 30, 120, 8]

# TODO: Create 'estimated_costs' by multiplying each token count by 0.002.
estimated_costs = []

# TODO: Create 'heavy_queries' including only token counts > 100.
heavy_queries = []

# TODO: Create 'labeled' strings: "{value}-High" if > 100 else "{value}-Low".
labeled = []

print("Challenge 3 - Labeled Tokens:", labeled)

# ==================================================================
# Challenge 4: The Matrix Flattener (The Token Mixer)
# ==================================================================
token_batches = [[12, 45, 10], [5, 8], [100, 20, 30]]

# TODO: Flatten 'token_batches' into a single list called 'all_tokens'.
all_tokens = []

print("Challenge 4 - Flat Tokens:", all_tokens)

# ==================================================================
# Challenge 5: The API Payload (Dictionaries)
# ==================================================================
chat_metadata = {
    "model": "llama-3.3",
    "status": "success",
    "tokens": [12, 45, 100]
}

# TODO: Update the "status" to "completed".
# TODO: Add a new key "finish_reason" with the value "stop".
# TODO: Access and print the second element (index 1) of the "tokens" list.
# TODO: Loop through the dictionary and print all keys and values.

print("Challenge 5 - Metadata:", chat_metadata)

# ==================================================================
# Challenge 6: Nested Extraction (The Response Parser)
# ==================================================================
api_responses = [
    {"id": 1, "choices": [{"text": "Hello!", "score": 0.9}]},
    {"id": 2, "choices": [{"text": "Python is cool", "score": 0.85}]},
    {"id": 3, "choices": [{"text": "Error 404", "score": 0.1}]}
]

# TODO: Extract the "text" value from the first choice of every response into 'all_texts'.
all_texts = []

print("Challenge 6 - Extracted Texts:", all_texts)

# ==================================================================
# Challenge 7: Dictionary Filtering
# ==================================================================
search_results = [
    {"prompt": "Hi", "tokens": 10},
    {"prompt": "Explain AI", "tokens": 150},
    {"prompt": "Python tips", "tokens": 80},
    {"prompt": "Deep Learning", "tokens": 300}
]

# TODO: Create 'expensive_prompts' containing only the prompt text where tokens > 100.
expensive_prompts = []

print("Challenge 7 - Expensive Prompts:", expensive_prompts)

# ==================================================================
# Challenge 8: Sets and Tuples (The Data Master)
# ==================================================================
models_used = ["llama-3", "gpt-4", "llama-3", "gemini", "gpt-4"]
server_config = ("192.168.1.1", 8080)
duplicate_tokens = [10, 20, 10, 30, 20]

# TODO: Create a Set called 'unique_models' to deduplicate 'models_used'.
unique_models = {}

# TODO: Print the first item of 'server_config'.
# TODO: Try to change server_config[1] to 433 inside a try/except block.

# TODO: Convert 'duplicate_tokens' to a Set, then back to a List called 'cleaned_tokens'.
cleaned_tokens = []

print("Challenge 8 - Unique Models:", unique_models)
print("Challenge 8 - Cleaned Tokens:", cleaned_tokens)

# ==================================================================
# Challenge 9: Error Handling (The Robust Agent)
# ==================================================================
bad_data = ['{"prompt": "hi"}', 'invalid-json', '{"prompt": "hello"}']
valid_prompts = []

# TODO: Loop through 'bad_data'. Use try/except to handle json.loads().
# Append successful "prompt" values to 'valid_prompts'.
# Catch json.JSONDecodeError and pass or print a warning.

print("Challenge 9 - Valid Prompts:", valid_prompts)


# ==================================================================
# ==================  NEW CHALLENGES BELOW  ========================
# ==================================================================


# ==================================================================
# Challenge 10: Dictionary Comprehension (The Score Mapper)
# ==================================================================
# You have a list of model names and a list of their benchmark scores.
# Goal: Build a dict mapping model name -> score using a dict comprehension.

model_names = ["llama-3", "gpt-4", "gemini", "mistral"]
benchmark_scores = [82.5, 95.0, 88.3, 79.1]

# TODO: Use zip() and a dict comprehension to create 'score_map'.
# Expected: {"llama-3": 82.5, "gpt-4": 95.0, ...}
score_map = {}

# TODO: Using 'score_map', create 'top_models' — a list of model names
# where the score is >= 85. Use a list comprehension on score_map.items().
top_models = []

print("Challenge 10 - Score Map:", score_map)
print("Challenge 10 - Top Models:", top_models)


# ==================================================================
# Challenge 11: Sorting & Ranking (The Leaderboard)
# ==================================================================
leaderboard = [
    {"model": "mistral",  "score": 79.1},
    {"model": "gpt-4",    "score": 95.0},
    {"model": "llama-3",  "score": 82.5},
    {"model": "gemini",   "score": 88.3},
]

# TODO: Sort 'leaderboard' in descending order by "score" using sorted() + a lambda.
# Store the result in 'ranked'.
ranked = []

# TODO: Print each model's rank (1-based), name, and score.
# Expected output format:  #1 gpt-4 — 95.0

print("Challenge 11 - Ranked Models:", [r["model"] for r in ranked])


# ==================================================================
# Challenge 12: Aggregation with a Dictionary (The Usage Stats Builder)
# ==================================================================
# Each entry represents one API call: which model was used and how many tokens.
usage_log = [
    {"model": "gpt-4",   "tokens": 120},
    {"model": "llama-3", "tokens": 45},
    {"model": "gpt-4",   "tokens": 300},
    {"model": "gemini",  "tokens": 80},
    {"model": "llama-3", "tokens": 200},
    {"model": "gpt-4",   "tokens": 60},
]

# TODO: Build 'usage_stats' — a dict where each key is a model name and
# the value is the TOTAL tokens used by that model across all log entries.
# Hint: use dict.get() with a default of 0 to accumulate.
usage_stats = {}

# TODO: Find and print the model with the highest total token usage.
# Hint: use max() with a key argument on usage_stats.items().

print("Challenge 12 - Usage Stats:", usage_stats)


# ==================================================================
# Challenge 13: Chained Comprehension & Filtering (The Pipeline)
# ==================================================================
raw_logs = [
    "  INFO: model loaded  ",
    "ERROR: timeout",
    "  INFO: request complete  ",
    "WARNING: high token count",
    "ERROR: invalid key",
    "  INFO: cache hit  ",
]

# TODO: In ONE list comprehension, strip each string AND keep only lines
# that start with "ERROR" after stripping. Store in 'error_logs'.
error_logs = []

# TODO: From 'error_logs', extract just the message part after "ERROR: "
# into 'error_messages'. (e.g., "timeout", "invalid key")
error_messages = []

print("Challenge 13 - Error Logs:", error_logs)
print("Challenge 13 - Error Messages:", error_messages)


# ==================================================================
# Challenge 14: Set Operations (The Model Auditor)
# ==================================================================
# Two teams ran experiments with different models.
team_alpha = {"gpt-4", "llama-3", "gemini", "mistral"}
team_beta = {"gpt-4", "claude-3", "mistral", "falcon"}

# TODO: Find models used by BOTH teams → 'common_models'  (intersection)
common_models = set()

# TODO: Find models used by EITHER team (no duplicates) → 'all_models'  (union)
all_models = set()

# TODO: Find models used by team_alpha but NOT team_beta → 'alpha_only'  (difference)
alpha_only = set()

# TODO: Find models used by exactly ONE team (not both) → 'exclusive_models' (symmetric difference)
exclusive_models = set()

print("Challenge 14 - Common:", common_models)
print("Challenge 14 - All:", all_models)
print("Challenge 14 - Alpha Only:", alpha_only)
print("Challenge 14 - Exclusive:", exclusive_models)


# ==================================================================
# Challenge 15: Named Tuples (The Structured Response)
# ==================================================================

# TODO: Define a namedtuple called 'APIResponse' with fields:
# request_id, model, tokens_used, status
APIResponse = None  # Replace with namedtuple definition

# TODO: Create a list 'responses' with at least 3 APIResponse instances.
responses = []

# TODO: Loop through 'responses' and print each one in the format:
# "[id] model=<model> tokens=<tokens> status=<status>"

# TODO: Using a list comprehension, extract all request_ids from 'responses'
# into 'response_ids'.
response_ids = []

print("Challenge 15 - Response IDs:", response_ids)


# ==================================================================
# Challenge 16: Nested Error Handling (The Batch Validator)
# ==================================================================
# A batch of raw API payloads — some are malformed in different ways.
batch_payloads = [
    '{"model": "gpt-4", "tokens": 100}',
    'not json at all',
    '{"model": "llama-3"}',          # missing "tokens" key
    '{"model": "gemini", "tokens": "abc"}',  # tokens is not an int
    '{"model": "mistral", "tokens": 50}',
]

validated = []

# TODO: Loop through 'batch_payloads'. For each one:
#   1. Try to parse it as JSON  → catch json.JSONDecodeError, print "Bad JSON: ..."
#   2. Try to access payload["tokens"] as an int  → catch KeyError, print "Missing key: ..."
#   3. Validate int() conversion  → catch ValueError, print "Bad value: ..."
#   4. If all passes, append {"model": ..., "tokens": <int>} to 'validated'.

print("Challenge 16 - Validated Payloads:", validated)


# ==================================================================
# Challenge 17: Building an Inverted Index (The Keyword Search Engine)
# ==================================================================
# Each document is a simple string. Build an index: word → list of doc ids.
documents = [
    "python is great for AI",
    "AI and machine learning with python",
    "deep learning models in python",
    "data science and AI tools",
]

# TODO: Build 'index' — a dict where each key is a unique word (lowercased)
# and the value is a sorted list of document indices (0-based) where the word appears.
# Example: {"python": [0, 1, 2], "ai": [0, 1, 3], ...}
index = {}

# TODO: Use 'index' to find all document indices that contain the word "ai".
# Store in 'ai_docs'.
ai_docs = []

print("Challenge 17 - 'ai' appears in docs:", ai_docs)
print("Challenge 17 - Index sample for 'python':", index.get("python"))


# ==================================================================
# Challenge 18: Bringing It All Together (The Mini Analytics Pipeline)
# ==================================================================
# A realistic dataset of LLM request logs.
request_logs = [
    {"session": "s1", "model": "gpt-4",   "tokens": 250, "status": "success"},
    {"session": "s2", "model": "llama-3", "tokens": 80,  "status": "error"},
    {"session": "s3", "model": "gpt-4",   "tokens": 400, "status": "success"},
    {"session": "s4", "model": "gemini",  "tokens": 120, "status": "success"},
    {"session": "s5", "model": "llama-3", "tokens": 300, "status": "success"},
    {"session": "s6", "model": "gpt-4",   "tokens": 90,  "status": "error"},
    {"session": "s7", "model": "gemini",  "tokens": 210, "status": "success"},
]

# TODO 1: Using a list comprehension, create 'successful_logs' — only entries
# where status == "success".
successful_logs = []

# TODO 2: Using a set comprehension, create 'models_with_errors' — model names
# that appear in at least one "error" log entry.
models_with_errors = set()

# TODO 3: Build 'token_summary' — a dict mapping each model to its AVERAGE
# token count across ALL logs (not just successful ones). Round to 2 decimal places.
token_summary = {}

# TODO 4: Find the session ID of the single most expensive successful request
# (highest tokens among successful_logs). Store in 'top_session'.
top_session = None

# TODO 5: Using 'token_summary', build a sorted list of tuples (model, avg_tokens)
# ordered from highest to lowest average tokens. Store in 'model_ranking'.
model_ranking = []

print("Challenge 18 - Successful logs count:", len(successful_logs))
print("Challenge 18 - Models with errors:", models_with_errors)
print("Challenge 18 - Token Summary:", token_summary)
print("Challenge 18 - Top Session:", top_session)
print("Challenge 18 - Model Ranking:", model_ranking)
