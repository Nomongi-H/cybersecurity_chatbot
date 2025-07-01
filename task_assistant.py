import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime, timedelta

# List to store tasks in memory
tasks = []

# Adds a new task to the list
def add_task():
    title = simpledialog.askstring("Add Task", "Enter task title:")
    if not title:
        return

    description = simpledialog.askstring("Add Task", "Enter task description:")
    if not description:
        return

    reminder = simpledialog.askstring("Reminder (optional)", "Remind me in how many days? (leave blank if none):")
    reminder_date = None

    if reminder and reminder.isdigit():
        reminder_date = datetime.now() + timedelta(days=int(reminder))

    task = {
        "title": title,
        "description": description,
        "reminder": reminder_date,
        "completed": False
    }

    tasks.append(task)
    messagebox.showinfo("Success", f"✅ Task '{title}' added!")

# Show list of tasks
def view_tasks():
    if not tasks:
        messagebox.showinfo("Tasks", "📭 No tasks available.")
        return

    task_list = ""
    for i, task in enumerate(tasks):
        status = "✅ Done" if task["completed"] else "❌ Pending"
        reminder = f"⏰ Reminder: {task['reminder'].strftime('%Y-%m-%d')}" if task["reminder"] else ""
        task_list += f"{i+1}. {task['title']} - {status}\n   📄 {task['description']}\n   {reminder}\n\n"

    messagebox.showinfo("Your Tasks", task_list)

# Mark a task as complete
def complete_task():
    if not tasks:
        messagebox.showinfo("Tasks", "No tasks to complete.")
        return

    index = simpledialog.askinteger("Complete Task", "Enter task number to mark as complete:")
    if index and 0 < index <= len(tasks):
        tasks[index-1]["completed"] = True
        messagebox.showinfo("Success", "🎉 Task marked as complete.")
    else:
        messagebox.showerror("Error", "Invalid task number.")

# Delete a task
def delete_task():
    if not tasks:
        messagebox.showinfo("Tasks", "No tasks to delete.")
        return

    index = simpledialog.askinteger("Delete Task", "Enter task number to delete:")
    if index and 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        messagebox.showinfo("Deleted", f"🗑️ Task '{removed['title']}' deleted.")
    else:
        messagebox.showerror("Error", "Invalid task number.")

# Build the GUI
def open_task_assistant():
    window = tk.Tk()
    window.title("Cybersecurity Task Assistant")
    window.geometry("400x300")
    window.configure(bg="#e6f7ff")

    tk.Label(window, text="Cybersecurity Task Manager", bg="#e6f7ff", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Button(window, text="➕ Add Task", width=20, command=add_task).pack(pady=5)
    tk.Button(window, text="📋 View Tasks", width=20, command=view_tasks).pack(pady=5)
    tk.Button(window, text="✅ Complete Task", width=20, command=complete_task).pack(pady=5)
    tk.Button(window, text="🗑️ Delete Task", width=20, command=delete_task).pack(pady=5)
    tk.Button(window, text="❌ Close", width=20, command=window.destroy).pack(pady=20)

    window.mainloop()
