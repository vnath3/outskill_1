import json


def build_prompt():
    prompt = {"model": "gpt-3.5-turbo", "temperature": 0.7, "messages": [{"role": "system",
        "content": "You are a helpful assistant that extracts key information from text."}]}
    
    print(json.dumps(prompt, indent=4))


if __name__ == "__main__":
    build_prompt()