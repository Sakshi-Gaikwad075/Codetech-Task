# chatbot.py

import nltk
import random
import string

# Step 1: Sample conversation data
data = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I am fine, thank you!", "I am good, and you?"],
    "what is your name": ["I am a Chatbot.", "You can call me AI Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"]
}

# Step 2: Function to clean user input
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Step 3: Function to generate chatbot response
def chatbot_response(user_input):
    user_input = clean_text(user_input)
    for key in data.keys():
        if key in user_input:  # Check if user input matches a key
            return random.choice(data[key])
    return "Sorry, I don't understand that."  # Default response if no match

# Step 4: Chat loop
print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Bye! Have a nice day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)