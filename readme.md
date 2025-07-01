#  Cybersecurity Awareness Chatbot

A Python-based virtual assistant that educates users about cybersecurity topics through engaging conversation. Includes NLP simulation, sentiment detection, task reminders, a quiz mini-game, and activity logging — all integrated with GUI components.

---

## 📦 Features

- 🔊 Voice greeting with a warm welcome
- 🖼️ ASCII art logo for a custom launch screen
- 🤖 Chatbot with:
  - Predefined responses for cybersecurity topics (e.g., passwords, phishing)
  - Keyword recognition and NLP simulation
  - Sentiment detection and memory-based personalization
- 🗂️ Task Assistant with GUI:
  - Add/manage tasks with optional reminders
- 🧠 Quiz Game:
  - Cybersecurity multiple-choice and true/false questions
  - Score tracking and performance feedback
- 📋 Activity Log:
  - Tracks tasks, reminders, quiz activity, and interactions

---

## 🚀 How to Run the Program

### 🔧 Prerequisites

Make sure you have Python 3.8+ installed.

### 📁 Project Structure (Simplified)

```
CybersecurityChatbot/
├── chatbot.py                # Main chatbot logic (CLI)
├── ascii.py                  # ASCII logo function
├── voice_greeting.py         # Voice greeting playback
├── task_assistant.py         # GUI Task Assistant
├── quiz_game.py              # GUI Quiz mini-game
├── nlp_utils.py              # NLP string keyword/intents
├── assets/                   # Contains logo image/audio if needed
└── README.md
```

---

## 📥 Installation & Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/CybersecurityChatbot.git
cd CybersecurityChatbot
```

### 2. Create Virtual Environment *(optional but recommended)*

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Install Required Packages


> Install manually:

```bash
pip install colorama
pip install playsound
pip install pillow
```

### 4. Add Audio File *(Optional)*

Ensure your `voice_greeting.mp3` or `.wav` file is in the correct path and referenced in `voice_greeting.py`

---

## ▶️ Running the Program

To start the chatbot:
Run the file:
python chatbot.py

Once launched, you can:

- Interact with the bot
- Type `task assistant` to manage cybersecurity tasks (GUI)
- Type `cyber quiz` to take a cybersecurity quiz (GUI)
- Type `exit` to leave the conversation

---

## ✅ How to Test the Program

### 🧪 Functional Testing

| Feature       | Test Input                     | Expected Output                 |
| ------------- | ------------------------------ | ------------------------------- |
| Greeting      | Launch script                  | Voice + ASCII art + name prompt |
| Chat Response | "Tell me about passwords"      | Password tips response          |
| Sentiment     | "I feel frustrated"            | Comforting message              |
| Task          | "Add a task to review privacy" | Task added + reminder option    |
| Reminder      | "Remind me to update password" | Reminder confirmation           |
| Quiz          | Type `cyber quiz`              | Launches quiz window            |
| Activity Log  | "Activity log"                 | Lists last 5–10 actions         |

### 🛠 Debugging Tips

- If GUI windows don’t appear → Check for `tkinter` installation:

```bash
sudo apt install python3-tk       # Ubuntu/Debian
brew install python-tk            # macOS
```

- If audio doesn’t play → Check `playsound` and audio file path

---

## Cyber Topics Covered

- Password safety
- Scams
- Privacy settings
- Social engineering
- Safe web browsing
- Two-factor authentication

---

## 📚 Dependencies

| Package              | Use                         |
| -------------------- | --------------------------- |
| `colorama`           | Terminal color output       |
| `playsound`          | Audio greeting playback     |
| `tkinter`            | GUI task assistant and quiz |
| `random`, `datetime` | Built-in Python modules     |

---

## 🧠 Credits

Developed by Nomongi-H. Feel free to fork, enhance, and build your own educational bots!

---

## 🔐 Stay Safe Online!

"Knowledge is the best firewall."

