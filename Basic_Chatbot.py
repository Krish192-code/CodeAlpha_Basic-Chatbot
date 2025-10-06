def chatbot():

    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in ['bye', 'goodbye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif user_input in ['hello', 'hi', 'hey', 'hola']:
            print("Chatbot: Hi! How can I help you?")
        
        elif user_input in ['how are you', 'how are you doing', "how's it going"]:
            print("Chatbot: I'm fine, thanks! How about you?")
        
        elif user_input in ['what is your name', 'who are you', 'your name']:
            print("Chatbot: I'm a simple rule-based chatbot!")
        
        elif user_input in ['help', 'what can you do']:
            print("Chatbot: I can respond to basic greetings like hello, how are you, etc.")
        
        elif user_input in ['thank you', 'thanks']:
            print("Chatbot: You're welcome!")
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Try saying 'hello' or 'how are you'?")

if __name__ == "__main__":

    chatbot()
