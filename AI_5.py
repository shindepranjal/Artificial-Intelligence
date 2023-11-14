# Pranjali Shinde(TA63)  Experiment 5: Chatbot


import random

rules = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm a chatbot, but I'm doing fine."],
    "what's your name": ["I'm a chatbot.", "I don't have a name, call me ChatBot."],
    "bye": ["Goodbye!", "See you later!"],
}


def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in rules:
        if key in user_input:
            return random.choice(rules[key])
    return "I'm sorry, I don't understand."


# Main loop for chatting
print("Hello! I'm a simple chatbot. You can start a conversation or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("ChatBot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)
