#  build a basic AI models (this is call a random chartbort) Rule-based

def chatbot(input_text):

    response = {
        "hello": "Hi there!",
        "how are you": "I'm just a bot, but I'm good!",
        "bye":"Goobye!"
    }
    return response.get(input_text.lower(), "sorry, I don't understand.")
for i in range(3):
 user_input = input("You: ")
 print("Bot: ", chatbot(user_input))  