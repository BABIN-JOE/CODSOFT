def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert the input to lowercase for easier matching

    # Greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"
    elif "good morning" in user_input:
        return "Good morning! How can I assist you today?"
    elif "good afternoon" in user_input:
        return "Good afternoon! How can I help you today?"
    elif "good evening" in user_input:
        return "Good evening! How can I assist you today?"
    
    # Small Talk
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what's up" in user_input:
        return "Not much! I'm here to help you. What can I do for you?"
    elif "how's it going" in user_input:
        return "It's going well! How can I assist you today?"

    # Personal Questions
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm a chatbot created to assist you. You can call me ChatBot!"
    elif "your age" in user_input:
        return "I don't have an age like humans do, but I was created recently."
    elif "creator" in user_input or "created" in user_input:
        return "I was created by a Software Developer Called Babin Joe."

    # Ending the Conversation
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Default Response
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Simulate a conversation
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("ChatBot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)
