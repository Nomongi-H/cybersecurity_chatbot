# Import module for playing sound
from playsound import playsound

# Function to play a welcome voice greeting
def play_greeting():
    try:
        playsound("C:\\Users\\NomongiHlatshwayo\\Downloads\\cybersecurity_chatbot\\Voice_greeting.mp3")  # Path to the audio file
    except Exception as e:
        print("Error playing sound:", e)
