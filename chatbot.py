from voice_greeting import play_greeting
from ascii import display_logo

from colorama import Fore, Style, init
import time
import os
import random

# Initialize colorama (coloured text on all platforms)
init(autoreset=True)  

# Store user data and conversation memory
memory = {
    "name": None,
    "favorite_topic": None,
    "last_topic": None,
}


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
    #Calling the implemented functions
    play_greeting()  # Play the recorded welcome message
    display_logo()  # Show ASCII art logo
    clear_screen() #clears the screen
    
    print(Fore.CYAN + "=" * 100)
    slow_print(Fore.YELLOW + "🤖 Hello! Welcome to the Cybersecurity Awareness Bot")
    print(Fore.CYAN + "=" * 60)

    name = input(Fore.GREEN + "📝 What's your name? ").strip()

    while not name:
        print(Fore.RED + "⚠️ Name cannot be empty.")
        name = input(Fore.GREEN + "📝 Please enter your name: ").strip()
        
    memory["name"] = name
    slow_print(Fore.MAGENTA + f"👋 Nice to meet you, {name}!")
    print(Fore.CYAN + "-" * 100)
    slow_print(Fore.YELLOW + "💡 Tip: Try asking me about phishing, password safety, or safe browsing.")
    print(Fore.CYAN + "-" * 100)
    return name


# # function with dictionary to store predefined responses
# def chatbot_response(user_input):
#     responses = {
#         "how are you?": "I'm not a human, I'm just a bot here to help you learn cybersecurity!",
#         "what's your purpose?": "My purpose is to educate you on key cybersecurity topics.",
#         "what can i ask you?": "You can ask me about:\n- Password Safety\n- Phishing Scams\n- Safe Browsing Tips",
#         "password safety?": "Always use strong, unique passwords. Avoid using the same password for multiple sites and enable two-factor authentication.",
#         "phishing?": "Phishing is a scam where attackers trick you into giving personal info. Always check sender addresses and don’t click suspicious links.",
#         "safe browsing?": "Use secure (HTTPS) websites, avoid downloading from unknown sources, and keep your browser updated.",
#     }
    
#     # Normalize input to lowercase
#     key = user_input.lower().strip()

#     if key in responses:
#         return responses[key]
#     else:
#         return "Sorry, I didn't understand that. Try asking about cybersecurity topics."

# Predefined keyword-based responses
keyword_responses = {
    "password": [
        "🔐 Always use a strong, unique password with letters, numbers, and symbols.",
        "🔑 Don’t reuse passwords! Use a password manager to keep them safe.",
        "🛡️ Enable two-factor authentication for extra security."
    ],
    "scam": [
        "🎣 Watch for urgent messages asking for money or account info.",
        "⚠️ Scammers often impersonate trusted companies. Double-check URLs.",
        "📩 Don’t click unknown email links or download attachments."
    ],
    "privacy": [
        "🔒 Limit the personal info you share on social media.",
        "🕵️‍♂️ Use browser privacy settings and trackers blockers.",
        "🌐 Use a VPN when browsing on public Wi-Fi."
    ]
}

# Sentiment detection dictionary
sentiments = {
    "worried": "😟 It’s okay to be concerned — cybersecurity can feel tricky, but you’re doing great learning it!",
    "frustrated": "😣 Don’t worry. If something confuses you, I can explain it differently!",
    "curious": "🤓 I love curiosity! Ask me anything you want to know about staying safe online."
}

# Recognize keywords in sentences
def detect_keywords(user_input):
    for keyword in keyword_responses:
        if keyword in user_input.lower():
            memory["last_topic"] = keyword  # remember current topic
            return keyword
    return None

# Recognize sentiment from the user
def detect_sentiment(user_input):
    for feeling in sentiments:
        if feeling in user_input.lower():
            return sentiments[feeling]
    return None

# Respond to user
def generate_response(user_input):
    user_input = user_input.lower().strip()

    # Exit condition
    if user_input in ["exit", "quit"]:
        return "👋 Thanks for chatting! Stay safe, " + memory.get("name", "user") + "."

    # Detect sentiment
    mood_response = detect_sentiment(user_input)
    if mood_response:
        return mood_response

    # Keyword match
    keyword = detect_keywords(user_input)
    if keyword:
        if memory["favorite_topic"] is None:
            memory["favorite_topic"] = keyword  # save first topic they asked about
        return random.choice(keyword_responses[keyword])

    # Handle follow-up on last topic
    if "more" in user_input or "tell me more" in user_input:
        if memory["last_topic"]:
            return "🔁 Here's more info on " + memory["last_topic"] + ":\n" + random.choice(keyword_responses[memory["last_topic"]])
        else:
            return "🤔 Could you tell me which topic you'd like to know more about?"

    # Random fallback
    return "❓ I didn’t quite get that. You can ask me about password safety, scams, or privacy tips."


def main():
    user_name = greet_user()
    print(Fore.YELLOW + f"\n💬 Hello {user_name}, ask me anything about cybersecurity (type 'exit' to quit).\n")

    while True:
        user_input = input(Fore.LIGHTGREEN_EX + f"{user_name} 🧑‍💻 > ")
       
        if user_input in ["exit", "quit"]:
            slow_print(Fore.YELLOW + f"👋 Thanks for chatting, {user_name}! Stay safe online.")
            break

        print(Fore.LIGHTCYAN_EX + "🤖 Bot is typing...\n")
        time.sleep(1)

        response = generate_response(user_input)
        slow_print(Fore.WHITE + f"{response}")

        print(Fore.CYAN + "\n" + "=" * 100)

if __name__ == "__main__":
    main()
