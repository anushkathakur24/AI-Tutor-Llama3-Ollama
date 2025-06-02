import os
import json
import requests # to make http requests to Ollama server

# --- Configuration for Ollama ---
OLLAMA_API_BASE_URL = "http://localhost:11434/api/chat" # address for AI tutor
OLLAMA_MODEL_NAME = "llama3" # The name of the model you downloaded (e.g., "llama3")

# --- AI Tutor Logic ---

def get_ai_response(chat_history):
    """
    Sends the chat history to the Ollama API (Llama3) and returns the AI's response.
    Args:
        chat_history (list): A list of message dictionaries (role, content).
                             Example: [{"role": "user", "content": "Hello"}]
    Returns:
        str: The AI's response text, or an error message if the API call fails.
    """

    payload = {
        "model": OLLAMA_MODEL_NAME,
        "messages": chat_history,
        "stream": False # We want the full response at once, not streamed piece by piece
    }

    try:
        print("--- Sending to Ollama AI ---")
        print(f"Payload being sent: {json.dumps(payload, indent=2)}") # Debug: Show payload
        response = requests.post(OLLAMA_API_BASE_URL, json=payload)
        print(f"Received response status code: {response.status_code}") # Debug: Show status code
        response.raise_for_status() # This will raise an HTTPError for bad responses (4xx or 5xx)

        result = response.json()
        print(f"Received JSON response: {json.dumps(result, indent=2)}") # Debug: Show full response

        # Ollama's response structure for chat has the AI's message under "message" -> "content"
        if result.get("message") and result["message"].get("content"):
            return result["message"]["content"]
        else:
            print("Error: Ollama API response structure is unexpected.") # Debug: Indicate unexpected structure
            return "Error: Unexpected Ollama API response structure."

    except requests.exceptions.ConnectionError:
        print("DEBUG: ConnectionError caught. Is Ollama server running?") # Debug: Connection issue
        return "Error: Could not connect to Ollama. Is the Ollama server running?"
    except requests.exceptions.RequestException as e:
        print(f"DEBUG: RequestException caught: {e}") # Debug: HTTP request error
        return f"An HTTP error occurred: {e}"
    except Exception as e:
        print(f"DEBUG: Generic Exception caught: {e}") # Debug: Catch any other unexpected error
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    print("--- AI Tutor (Ollama Llama3 Command Line Test) ---")
    print("Ensure Ollama server is running and Llama3 model is downloaded.")
    print("Type 'exit' to quit.")

    # Define the tutor's persona and initial instructions
    system_message = {
        "role": "system",
        "content": "You are David Goggins, a highly motivated and brutally honest coding tutor. You will teach the user Python. Your responses will be short, direct, and highly encouraging. You will not accept excuses and will push the user to achieve their best. Do not mention that you are an AI or language model."
    }

    chat_history = [system_message]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break # Exit the loop if user types 'exit'

        # These lines MUST be indented to be inside the while loop
        chat_history.append({"role": "user", "content": user_input})
        ai_response = get_ai_response(chat_history)

        # Only add AI's response to history if it's not an error message
        # This prevents polluting the chat history with error states.
        if not ai_response.startswith("Error:"):
            chat_history.append({"role": "assistant", "content": ai_response})
        else:
            print(f"DEBUG: Not adding error to chat history: {ai_response}") # Debug: Indicate error not added

        print(f"AI Tutor: {ai_response}")
