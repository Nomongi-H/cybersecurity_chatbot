# from voice_greeting import play_greeting
from ascii import display_logo

from colorama import Fore, Style, init
import time
import os

# Initialize colorama
init(autoreset=True)

# Function to simulate a typewriter effect
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # newline

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Ask the user's name
def greet_user():
    # play_greeting()  # Play the recorded welcome message
    display_logo()  # Show ASCII art logo
    print(Fore.CYAN + "=" * 100)
    slow_print(Fore.YELLOW + "🤖 Hello! Welcome to the Cybersecurity Awareness Bot")
    print(Fore.CYAN + "=" * 60)

    name = input(Fore.GREEN + "📝 What's your name? ").strip()

    while not name:
        print(Fore.RED + "⚠️ Name cannot be empty.")
        name = input(Fore.GREEN + "📝 Please enter your name: ").strip()
        
    slow_print(Fore.MAGENTA + f"👋 Nice to meet you, {name}!")
    print(Fore.CYAN + "-" * 100)
    slow_print(Fore.YELLOW + "💡 Tip: Try asking me about phishing, password safety, or safe browsing.")
    print(Fore.CYAN + "-" * 100)
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
        print(Fore.BLUE + "\n💬 Type 'exit' to quit at any time.")
        user_input = input(Fore.LIGHTGREEN_EX + f"\n{user_name} 🧑‍💻 > ").strip()

        if user_input.lower() in ['exit', 'quit']:
            slow_print(Fore.YELLOW + "👋 Goodbye! Stay safe online.")
            break

        print(Fore.LIGHTCYAN_EX + "\n🤖 Bot is typing...\n")
        time.sleep(1)  # Simulate thinking

        response = chatbot_response(user_input)
        slow_print(Fore.WHITE + f"🔐 Bot: {response}")

        print(Fore.CYAN + "\n" + "=" * 100)

if __name__ == "__main__":
    main()
