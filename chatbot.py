from quiz_game import start_quiz
from task_assistant import open_task_assistant
from voice_greeting import play_greeting
from ascii import display_logo
from colorama import Fore, Style, init
from nlp_utils import detect_intent, extract_task_description, extract_reminder_details

import time
import datetime
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

user_actions = []  # Memory for NLP-based task/reminder logging
activity_log = []  # Store logs of actions performed


# Function to simulate a typewriter effect
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # newline

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def log_action(action_description):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {action_description}"
    activity_log.append(entry)
    # Limit log to 50 entries
    if len(activity_log) > 50:
        activity_log.pop(0)


# Ask the user's name
def greet_user():
    play_greeting()       # Voice greeting
    clear_screen()        # Clears terminal screen
    display_logo()        # ASCII logo
    

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

# Predefined keyword-based responses
keyword_responses = {
    "password": [
        "🔐 Always use a strong, unique password with letters, numbers, and symbols.",
        "🔑 Don’t reuse passwords! Use a password manager to keep them safe.",
        "🪪 Enable two-factor authentication for extra security."
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
            memory["last_topic"] = keyword
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

    # Detect sentiment
    mood_response = detect_sentiment(user_input)
    if mood_response:
        return mood_response

    # Keyword match
    keyword = detect_keywords(user_input)
    if keyword:
        if memory["favorite_topic"] is None:
            memory["favorite_topic"] = keyword
        return random.choice(keyword_responses[keyword])

    # Handle follow-up on last topic
    if "more" in user_input or "tell me more" in user_input:
        if memory["last_topic"]:
            return "🔁 Here's more info on " + memory["last_topic"] + ":\n" + random.choice(keyword_responses[memory["last_topic"]])
        else:
            return "🤔 Could you tell me which topic you'd like to know more about?"

    return "❓ I didn’t quite get that. You can ask me about password safety, scams, or privacy tips."


def main():
    user_name = greet_user()
    print(Fore.YELLOW + f"\n💬 Hello {user_name}, ask me anything about cybersecurity (type 'exit' to quit).\n")

    while True:
        user_input = input(Fore.LIGHTGREEN_EX + f"{user_name} 🧑‍💻 > ").strip().lower()

        # NLP intent detection
        intent = detect_intent(user_input)

        if intent == "set_reminder":
            reminder = extract_reminder_details(user_input)
            if reminder:
                user_actions.append(f"Reminder set for \"{reminder}\"")
                slow_print(Fore.MAGENTA + f"📅 Reminder set for \"{reminder}\".")
                log_action(f"Reminder set: \"{reminder}\"")
            else:
                slow_print(Fore.RED + "❗ Sorry, I couldn’t understand what to remind you about.")
            continue

        elif intent == "add_task":
            task = extract_task_description(user_input)
            if task:
                user_actions.append(f"Task added: \"{task}\", no reminder set")
                slow_print(Fore.GREEN + f"📝 Task added: {task}. Would you like to set a reminder for this task?")
                log_action(f"Task added: \"{task}\", no reminder set")
            else:
                slow_print(Fore.RED + "❗ I couldn't extract a task description.")
            continue

        elif intent == "show_summary":
            if user_actions:
                slow_print(Fore.BLUE + "📋 Here's a summary of recent actions:")
                for i, action in enumerate(user_actions, 1):
                    print(Fore.LIGHTBLUE_EX + f"{i}. {action}")
            else:
                slow_print(Fore.YELLOW + "🕵️ No tasks or reminders have been set yet.")
            continue

        elif intent == "start_quiz":
            print(Fore.CYAN + "🎮 Launching the Cybersecurity Quiz...")
            start_quiz()
            log_action("Quiz started")
            continue

        elif intent == "show_activity_log":
            log_action("Viewed activity log")
            if activity_log:
                slow_print(Fore.BLUE + "📋 Recent activity log:")
                for i, entry in enumerate(activity_log[-10:], 1):  # Show last 10 actions
                    print(Fore.LIGHTBLUE_EX + f"{i}. {entry}")
            else:
                slow_print(Fore.YELLOW + "🕵️ No recent activity to show.")
            continue
        
        elif user_input in ["exit"]:
            slow_print(Fore.YELLOW + f"👋 Thanks for chatting, {user_name}! Stay safe online.")
            break

        elif user_input == "task assistant":
            print(Fore.GREEN + "🔧 Launching your Cybersecurity Task Assistant...")
            open_task_assistant()
            continue

        print(Fore.LIGHTCYAN_EX + "🤖 Bot is typing...\n")
        time.sleep(1)
        response = generate_response(user_input)
        slow_print(Fore.WHITE + f"{response}")
        keyword = detect_keywords(user_input)
        #Keyword was not detected
        # Added a log action to tack any matches
        if keyword: 
            log_action(f"Keyword topic discussed: {keyword}") 
    
        print(Fore.CYAN + "\n" + "=" * 100)


if __name__ == "__main__":
    main()


 
# from quiz_game import start_quiz
# from task_assistant import open_task_assistant
# from voice_greeting import play_greeting
# from ascii import display_logo
# from colorama import Fore, Style, init
# from nlp_utils import detect_intent, extract_task_description, extract_reminder_details


# import time
# import os
# import random

# # Initialize colorama (coloured text on all platforms)
# init(autoreset=True)  

# # Store user data and conversation memory
# memory = {
#     "name": None,
#     "favorite_topic": None,
#     "last_topic": None,
# }



# # Function to simulate a typewriter effect
# def slow_print(text, delay=0.03):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(delay)
#     print()  # newline

# # Clear screen
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')
    
# # Ask the user's name
# def greet_user():
#     #Calling the implemented functions
#     play_greeting()  # Play the recorded welcome message
#     display_logo()  # Show ASCII art logo
#     clear_screen() #clears the screen
    
#     print(Fore.CYAN + "=" * 100)
#     slow_print(Fore.YELLOW + "🤖 Hello! Welcome to the Cybersecurity Awareness Bot")
#     print(Fore.CYAN + "=" * 60)

#     name = input(Fore.GREEN + "📝 What's your name? ").strip()

#     while not name:
#         print(Fore.RED + "⚠️ Name cannot be empty.")
#         name = input(Fore.GREEN + "📝 Please enter your name: ").strip()
        
#     memory["name"] = name
#     slow_print(Fore.MAGENTA + f"👋 Nice to meet you, {name}!")
#     print(Fore.CYAN + "-" * 100)
#     slow_print(Fore.YELLOW + "💡 Tip: Try asking me about phishing, password safety, or safe browsing.")
#     print(Fore.CYAN + "-" * 100)
#     return name

# # Predefined keyword-based responses
# keyword_responses = {
#     "password": [
#         "🔐 Always use a strong, unique password with letters, numbers, and symbols.",
#         "🔑 Don’t reuse passwords! Use a password manager to keep them safe.",
#         "🛡️ Enable two-factor authentication for extra security."
#     ],
#     "scam": [
#         "🎣 Watch for urgent messages asking for money or account info.",
#         "⚠️ Scammers often impersonate trusted companies. Double-check URLs.",
#         "📩 Don’t click unknown email links or download attachments."
#     ],
#     "privacy": [
#         "🔒 Limit the personal info you share on social media.",
#         "🕵️‍♂️ Use browser privacy settings and trackers blockers.",
#         "🌐 Use a VPN when browsing on public Wi-Fi."
#     ]
# }

# # Sentiment detection dictionary
# sentiments = {
#     "worried": "😟 It’s okay to be concerned — cybersecurity can feel tricky, but you’re doing great learning it!",
#     "frustrated": "😣 Don’t worry. If something confuses you, I can explain it differently!",
#     "curious": "🤓 I love curiosity! Ask me anything you want to know about staying safe online."
# }

# # Recognize keywords in sentences
# def detect_keywords(user_input):
#     for keyword in keyword_responses:
#         if keyword in user_input.lower():
#             memory["last_topic"] = keyword  # remember current topic
#             return keyword
#     return None

# # Recognize sentiment from the user
# def detect_sentiment(user_input):
#     for feeling in sentiments:
#         if feeling in user_input.lower():
#             return sentiments[feeling]
#     return None

# # Respond to user
# def generate_response(user_input):
#     user_input = user_input.lower().strip()

#     # Exit condition
#     if user_input in ["exit", "quit"]:
#         return "👋 Thanks for chatting! Stay safe, " + memory.get("name", "user") + "."

#     # Detect sentiment
#     mood_response = detect_sentiment(user_input)
#     if mood_response:
#         return mood_response

#     # Keyword match
#     keyword = detect_keywords(user_input)
#     if keyword:
#         if memory["favorite_topic"] is None:
#             memory["favorite_topic"] = keyword  # save first topic they asked about
#         return random.choice(keyword_responses[keyword])

#     # Handle follow-up on last topic
#     if "more" in user_input or "tell me more" in user_input:
#         if memory["last_topic"]:
#             return "🔁 Here's more info on " + memory["last_topic"] + ":\n" + random.choice(keyword_responses[memory["last_topic"]])
#         else:
#             return "🤔 Could you tell me which topic you'd like to know more about?"

#     # Random fallback
#     return "❓ I didn’t quite get that. You can ask me about password safety, scams, or privacy tips."


# def main():
#     user_name = greet_user()
#     print(Fore.YELLOW + f"\n💬 Hello {user_name}, ask me anything about cybersecurity (type 'exit' to quit).\n")

#     while True:
#         user_input = input(Fore.LIGHTGREEN_EX + f"{user_name} 🧑‍💻 > ")
       
#         if user_input in ["exit", "quit"]:
#             slow_print(Fore.YELLOW + f"👋 Thanks for chatting, {user_name}! Stay safe online.")
#             break

#         # Special command to open task assistant
#         if user_input == "task assistant":
#             print(Fore.GREEN + "🔧 Launching your Cybersecurity Task Assistant...")
#             open_task_assistant()
#             continue
        
#         if user_input == "cyber quiz":
#             print(Fore.CYAN + "🎮 Launching the Cybersecurity Quiz...")
#         start_quiz()
#         continue
    
#     print(Fore.LIGHTCYAN_EX + "🤖 Bot is typing...\n")
#     print("DEBUG: Passed exit check")
#     time.sleep(1)
#     response = generate_response(user_input)
#     slow_print(Fore.WHITE + f"{response}")
#     print(Fore.CYAN + "\n" + "=" * 100)

# if __name__ == "__main__":
#     main()
