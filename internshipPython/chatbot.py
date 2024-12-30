import nltk
import random
import re
import os
import sys

nltk_data_path = os.path.join(os.getenv('APPDATA'), 'nltk_data')
if not os.path.exists(os.path.join(nltk_data_path, 'tokenizers', 'punkt')):
    nltk.download('punkt', quiet=True)  # Only download if punkt is missing


responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["I'm not sure how to respond to that.", "Can you tell me more?", "Let's change the topic."]
}


def preprocess_input(user_input):
    user_input = user_input.lower()  # Convert to lowercase
    user_input = re.sub(r'\s+', ' ', user_input)  # Remove extra spaces
    return user_input.strip()


def get_response(user_input):
    user_input = preprocess_input(user_input)

    if any(greet in user_input for greet in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])
    elif any(bye in user_input for bye in ["bye", "goodbye", "see you"]):
        return random.choice(responses["goodbye"])
    elif any(thank in user_input for thank in ["thank", "thanks", "appreciate"]):
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()
