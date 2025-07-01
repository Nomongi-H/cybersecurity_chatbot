import re

def detect_intent(user_input):
    """Very basic NLP simulation using keyword and intent matching"""

    input_lower = user_input.lower()

    # Direct commands
    if "remind me" in input_lower or "set reminder" in input_lower:
        return "set_reminder"
    elif "add a task" in input_lower or "create a task" in input_lower:
        return "add_task"
    elif "quiz" in input_lower or "play game" in input_lower:
        return "start_quiz"
    elif "summary" in input_lower or "what have you done" in input_lower:
        return "show_summary"

    # Cyber-related topics (for Part 2 conversation)
    elif "password" in input_lower:
        return "password_tip"
    elif "phishing" in input_lower:
        return "phishing_tip"
    elif "privacy" in input_lower:
        return "privacy_tip"

    return "unknown"

def extract_task_description(user_input):
    """Extracts task description using regex or simple parsing"""
    match = re.search(r"(add a task|create a task)\s+to\s+(.*)", user_input.lower())
    if match:
        return match.group(2).strip().capitalize()
    return None

def extract_reminder_details(user_input):
    """Extracts reminder task description"""
    match = re.search(r"remind me to\s+(.*)", user_input.lower())
    if match:
        return match.group(1).strip().capitalize()
    return None
