# GPT4all local API integration
### Uses a sample function
import yaml
import gradio as gr
import json
import os
from openai import OpenAI

with open('character_config.yaml', 'r') as f:
    char_config = yaml.safe_load(f)

# Initialize OpenAI client pointing to local GPT4all API
client = OpenAI(
    api_key="not-needed",  # GPT4all doesn't require an API key
    base_url="http://localhost:4891/v1"  # Default GPT4all API endpoint
)

# Constants
HISTORY_FILE = char_config['history_file']
SYSTEM_PROMPT = char_config['presets']['default']['system_prompt']

# Initialize message history with system prompt
SYSTEM_MESSAGE = {
    "role": "system",
    "content": SYSTEM_PROMPT
}

# Load/save chat history
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []
    
    # Always start with system prompt
    return [SYSTEM_MESSAGE] + history

def save_history(history):
    # Remove system message before saving (we'll add it back on load)
    history_to_save = [msg for msg in history if msg.get("role") != "system"]
    with open(HISTORY_FILE, "w") as f:
        json.dump(history_to_save, f, indent=2)



def get_riko_response_no_tool(messages):
    # Call local GPT4all API with chat messages
    response = client.chat.completions.create(
        model="gpt4all",  # Model name doesn't matter for local GPT4all
        messages=messages,
        temperature=char_config.get('temperature', 0.7),
        max_tokens=char_config.get('max_tokens', 2048),
        stream=False,
    )

    return response


def llm_response(user_input):

    messages = load_history()

    # Append user message to memory
    messages.append({
        "role": "user",
        "content": user_input
    })

    riko_test_response = get_riko_response_no_tool(messages)

    # Extract the response text from GPT4all response
    assistant_message = riko_test_response.choices[0].message.content

    # Append assistant message to history
    messages.append({
        "role": "assistant",
        "content": assistant_message
    })

    save_history(messages)
    return assistant_message


if __name__ == "__main__":
    print('running main')