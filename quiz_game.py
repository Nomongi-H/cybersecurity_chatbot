import tkinter as tk
from tkinter import messagebox

# Question bank
questions = [
    {
        "question": "What should you do if you receive an email asking for your password?",
        "options": ["Reply with your password", "Delete the email", "Report the email as phishing", "Ignore it"],
        "answer": "Report the email as phishing"
    },
    {
        "question": "True or False: It's safe to use the same password for all accounts.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question": "Which of these is a strong password?",
        "options": ["123456", "mydogname", "Pa$$w0rd!2024", "qwerty"],
        "answer": "Pa$$w0rd!2024"
    },
    {
        "question": "What is phishing?",
        "options": ["Fishing in a lake", "A type of hacking", "Fake emails trying to steal info", "A secure login method"],
        "answer": "Fake emails trying to steal info"
    },
    {
        "question": "True or False: Public Wi-Fi is always safe to use for banking.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question": "Which is NOT a good security habit?",
        "options": ["Using 2FA", "Clicking unknown links", "Locking your screen", "Updating software"],
        "answer": "Clicking unknown links"
    },
    {
        "question": "How can you identify a secure website?",
        "options": ["It loads quickly", "It has a padlock and HTTPS", "It's colorful", "It has ads"],
        "answer": "It has a padlock and HTTPS"
    },
    {
        "question": "True or False: Antivirus software is useless today.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question": "Social engineering is:",
        "options": ["Building websites", "Using psychological tricks to steal info", "Fixing software bugs", "Encrypting emails"],
        "answer": "Using psychological tricks to steal info"
    },
    {
        "question": "Which should you do to secure your online accounts?",
        "options": ["Use weak passwords", "Share passwords with friends", "Use two-factor authentication", "Ignore security updates"],
        "answer": "Use two-factor authentication"
    },
]

# Global quiz state
current_q = 0
score = 0
selected_option = None  # will be created in start_quiz()

# Process submitted answer
def submit_answer(window, question_label, options_frame, next_btn):
    global current_q, score, selected_option

    answer = selected_option.get()
    correct = questions[current_q]["answer"]

    if answer == correct:
        score += 1
        messagebox.showinfo("Correct!", "✅ Correct! Well done.")
    else:
        messagebox.showinfo("Incorrect", f"❌ Oops! The correct answer was:\n{correct}")

    current_q += 1
    if current_q >= len(questions):
        show_result(window)
    else:
        load_question(question_label, options_frame)

# Show final score and feedback
def show_result(window):
    global score
    msg = f"You scored {score} out of {len(questions)}.\n\n"
    if score == 10:
        msg += "🌟 Perfect score! You're a cybersecurity champion!"
    elif score >= 7:
        msg += "🎉 Great job! You're a cybersecurity pro!"
    elif score >= 4:
        msg += "👍 Not bad. Keep learning to stay safe!"
    else:
        msg += "📘 Keep learning! Cybersecurity is important."

    messagebox.showinfo("Quiz Finished", msg)
    window.destroy()

# Load question and options
def load_question(question_label, options_frame):
    global selected_option
    question_label.config(text=f"Q{current_q + 1}: {questions[current_q]['question']}")
    selected_option.set(None)

    # Clear old options
    for widget in options_frame.winfo_children():
        widget.destroy()

    for option in questions[current_q]["options"]:
        tk.Radiobutton(
            options_frame, text=option, variable=selected_option,
            value=option, anchor='w', padx=10, font=("Arial", 12), bg="#f2f7ff"
        ).pack(fill="x", pady=2)

# Start the quiz
def start_quiz():
    global current_q, score, selected_option
    current_q = 0
    score = 0

    window = tk.Tk()
    window.title("Cybersecurity Quiz")
    window.geometry("500x400")
    window.config(bg="#f2f7ff")

    selected_option = tk.StringVar()  # ✅ Now correctly created after window

    tk.Label(window, text="Cybersecurity Awareness Quiz", font=("Arial", 16, "bold"), bg="#f2f7ff").pack(pady=10)

    question_label = tk.Label(window, text="", wraplength=460, justify="left", font=("Arial", 13), bg="#f2f7ff")
    question_label.pack(pady=10)

    options_frame = tk.Frame(window, bg="#f2f7ff")
    options_frame.pack()

    next_btn = tk.Button(window, text="Submit Answer", font=("Arial", 12), command=lambda: submit_answer(window, question_label, options_frame, next_btn))
    next_btn.pack(pady=20)

    load_question(question_label, options_frame)

    window.mainloop()
