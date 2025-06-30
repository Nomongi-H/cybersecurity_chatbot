# Ask the user's name
def greet_user():
    print("="*100)
    name = input("Hello! What's your name? ").strip()
    
    while not name:
        print("Name cannot be empty. Please enter your name.")
        name = input("What's your name? ").strip()
    
    print(f"\nWelcome, {name}! Ask me anything about cybersecurity.\n")
    return name

# function with dictionary to store predefined responses
def chatbot_response(user_input):
    responses = {
        "how are you?": "I'm not a human, I'm just a bot here to help you learn cybersecurity!",
        "what's your purpose?": "My purpose is to educate you on key cybersecurity topics.",
        "what can i ask you?": "You can ask me about:\n- Password Safety\n- Phishing Scams\n- Safe Browsing Tips",
        "password safety?": "Always use strong, unique passwords. Avoid using the same password for multiple sites and enable two-factor authentication.",
        "phishing?": "Phishing is a scam where attackers trick you into giving personal info. Always check sender addresses and don’t click suspicious links.",
        "safe browsing?": "Use secure (HTTPS) websites, avoid downloading from unknown sources, and keep your browser updated.",
    }
    
    # Normalize input to lowercase
    key = user_input.lower().strip()

    if key in responses:
        return responses[key]
    else:
        return "Sorry, I didn't understand that. Try asking about cybersecurity topics."

def main():
    user_name = greet_user()
    
    while True:
        user_input = input(f"{user_name}, what would you like to ask? (type 'exit' to quit): ")
        
        if user_input.lower() in ['exit']:
            print("Goodbye, Stay safe online!")
            break
        
        response = chatbot_response(user_input)
        print("\nBot:", response, "\n")

if __name__ == "__main__":
    main()
